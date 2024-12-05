import pandas as pd
import pickle
import statsmodels.api as sm
from scipy.stats import kruskal

# Load your dataset
with open("data.pkl", 'rb') as f:
    data = pickle.load(f)

# H3.1: Perform Kruskal-Wallis Test to assess differences in foreign investment across income levels
income_groups = data.groupby('8. What is your annual income in EUR after taxes? ')['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?'].apply(list)
kruskal_test = kruskal(*income_groups)

# H3.2: Logistic Regression for high/low foreign investment categorization
# Define high/low foreign investments based on a threshold (e.g., 50%)
data['High Foreign Investment'] = (data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?'] >= 50).astype(int)

# Prepare data for logistic regression
X_h3 = sm.add_constant(data[['8. What is your annual income in EUR after taxes? ', '9. If you stopped working today and liquidated all your assets (both financial and real estate), for how many months could you maintain your current lifestyle and spending habits? ']])
y_h3 = data['High Foreign Investment']

# Fit the logistic regression model
model_h3 = sm.Logit(y_h3, X_h3).fit()

# Display Results
print("H3: Income and Net Worth Impact on Foreign Investments\n")
print("Kruskal-Wallis Test Results (Income Levels and Foreign Investments):")
print(f"H-statistic: {kruskal_test.statistic:.4f}, P-value: {kruskal_test.pvalue:.4f}")

print("\nLogistic Regression Summary:")
print(model_h3.summary())
