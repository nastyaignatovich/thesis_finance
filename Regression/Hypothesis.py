import pandas as pd
import pickle
import statsmodels.api as sm
from scipy.stats import pearsonr, spearmanr

# Load your dataset
with open("data.pkl", 'rb') as f:
    data = pickle.load(f)

print(data.columns)

# Correlation Analysis
# Pearson Correlation
pearson_corr, pearson_pval = pearsonr(data['10. How would you rate your financial literacy?'], data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?'])

# Regression Analysis
X_h1 = sm.add_constant(data['10. How would you rate your financial literacy?'])
y_h1 = data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?']

# Fit the OLS regression model
model_h1 = sm.OLS(y_h1, X_h1).fit()

# Display Results
print("H1: Financial Literacy and International Portfolio Diversification\n")
print("Pearson Correlation:")
print(f"Correlation Coefficient: {pearson_corr:.4f}, P-value: {pearson_pval:.4f}")


print("\nLinear Regression Summary:")
print(model_h1.summary())
