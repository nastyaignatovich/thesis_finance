import pandas as pd
import pickle
import numpy as np
import statsmodels.api as sm

# Load the data
with open("../Regression/data.pkl", 'rb') as f:
    data = pickle.load(f)

# Define dependent variables (uncomment the one you want to use)
dependent_var = 'foreign_portfolio_pct'  # Option 1
#dependent_var = 'foreign_assets_pct'    # Option 2

# Define variables and their types
variables = {
    # Factor variables (will be converted to dummies if uncommented)
    'FACTORS': {},

    # Regular variables
    'REGULAR': {
        'age': True,
        'gender': True,
        'education_high': True,
        'income_medium': True,
        'income_high': True,
        'fin_literacy': True,
        'invest_confidence': True,
        'long_outlook_diff': True
    }
}

# Function to check data types and print information
def check_data_types(df):
    print("\nData Types Check:")
    print(df.dtypes)
    print("\nSample of data:")
    print(df.head())

# Print initial data info
print("Initial data info:")
check_data_types(data)

# Get active factor variables
active_factors = [var for var, is_active in variables['FACTORS'].items() if is_active]

# Create dummy variables for active factors
if active_factors:
    data_with_dummies = pd.get_dummies(data, columns=active_factors, drop_first=True, dtype=float)
else:
    data_with_dummies = data.copy()

# Get active regular variables
active_regular = [var for var, is_active in variables['REGULAR'].items() if is_active]

# Combine all independent variables
independent_vars = active_regular.copy()
if active_factors:
    dummy_columns = [col for col in data_with_dummies.columns if any(factor in col for factor in active_factors)]
    independent_vars.extend(dummy_columns)

# Prepare data
X = data_with_dummies[independent_vars]
y = data_with_dummies[dependent_var]

# Ensure all columns are float type
X = X.astype(float)
y = y.astype(float)

# Print information about the processed data
print("\nProcessed data info:")
check_data_types(X)

# Remove any rows with NaN values
valid_rows = ~(X.isna().any(axis=1) | y.isna())
X = X[valid_rows]
y = y[valid_rows]

print("\nNumber of rows removed due to NA:", sum(~valid_rows))

# Add constant for statsmodels
X = sm.add_constant(X)

# Fit OLS regression
model = sm.OLS(y, X)
results = model.fit()

# Print results
print("\nOLS Regression Results:")
print("=" * 80)
print("\nDependent Variable:", dependent_var)
print("\nIncluded Variables:")
print("Regular variables:", active_regular)
print("Factor variables:", active_factors)
if active_factors:
    print("Created dummy variables:", dummy_columns)
print("\n", results.summary())

# Save results as a table in Excel
summary_df = pd.DataFrame({
    'Variable': results.params.index,
    'Coefficient': results.params.values,
    'Std. Error': results.bse.values,
    't-Statistic': results.tvalues.values,
    'p-Value': results.pvalues.values
})

# Save to Excel
summary_df.to_excel('regression_results_table.xlsx', index=False)

print("\nRegression results saved as 'regression_results_table.xlsx'.")
