import pandas as pd
import pickle
import statsmodels.api as sm
from scipy.stats import pearsonr

# Load your dataset
with open("data.pkl", 'rb') as f:
    data = pickle.load(f)

# H4.1: Correlation Analysis
# Correlation between short-term domestic outlook and foreign investments
corr_short, pval_short = pearsonr(data['14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?'], data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?'])

# Correlation between long-term domestic outlook and foreign investments
corr_long, pval_long = pearsonr(data['15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?'], data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?'])

# H4.2: Regression Analysis
X_h4 = data[['14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?', '15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?']]
X_h4 = sm.add_constant(X_h4)  # Add constant for intercept
y_h4 = data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?']

# Fit the OLS regression model
model_h4 = sm.OLS(y_h4, X_h4).fit()

# Display Results
print("H4: Domestic Economic Outlook and Home Bias\n")
print("Correlation Analysis:")
print(f"Short-Term Outlook - Correlation: {corr_short:.4f}, P-value: {pval_short:.4f}")
print(f"Long-Term Outlook - Correlation: {corr_long:.4f}, P-value: {pval_long:.4f}")

print("\nRegression Summary:")
print(model_h4.summary())
