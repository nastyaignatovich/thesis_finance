import pandas as pd
import statsmodels.api as sm
from scipy.stats import kruskal

# Load your dataset
data = pd.read_excel('survey_answers.xlsx'')

# Rename columns for clarity (if needed)
data = data.rename(columns={
    '18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?': 'Percentage of Foreign Assets',
    '8. What is your annual income in EUR after taxes? ': 'Income Level',
    '9. If you stopped working today and liquidated all your assets (both financial and real estate), for how many months could you maintain your current lifestyle and spending habits?': 'Net Worth Proxy'
})

# Drop rows with missing data
data = data.dropna(subset=['Income Level', 'Net Worth Proxy', 'Percentage of Foreign Assets'])

# Categorize Income Levels if not numerical
# Example map for categorizing (you can adjust this as needed):
income_map = {
    'Below 15 000': 0,
    'Between 15 000 and 40 000': 1,
    'Between 40 000 and 60 000': 2,
    'More than 60 000': 3
}
data['Income Level Numeric'] = data['Income Level'].map(income_map)

# H3.1: Perform Kruskal-Wallis Test to assess differences in foreign investment across income levels
income_groups = data.groupby('Income Level Numeric')['Percentage of Foreign Assets'].apply(list)
kruskal_test = kruskal(*income_groups)

# H3.2: Logistic Regression for high/low foreign investment categorization
# Define high/low foreign investments based on a threshold (e.g., 50%)
data['High Foreign Investment'] = (data['Percentage of Foreign Assets'] >= 50).astype(int)

# Prepare data for logistic regression
X_h3 = sm.add_constant(data[['Income Level Numeric', 'Net Worth Proxy']])
y_h3 = data['High Foreign Investment']

# Fit the logistic regression model
model_h3 = sm.Logit(y_h3, X_h3).fit()

# Display Results
print("H3: Income and Net Worth Impact on Foreign Investments\n")
print("Kruskal-Wallis Test Results (Income Levels and Foreign Investments):")
print(f"H-statistic: {kruskal_test.statistic:.4f}, P-value: {kruskal_test.pvalue:.4f}")

print("\nLogistic Regression Summary:")
print(model_h3.summary())
