import pandas as pd
import pickle
import statsmodels.api as sm
from scipy.stats import f_oneway

# Load the dataset
with open("data.pkl", 'rb') as f:
    data = pickle.load(f)

print(data.columns)

# Calculate Domestic Investment Percentage
data['Domestic Investment Percentage'] = 100 - data['18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?']

# ANOVA: Short-Term Domestic Outlook and Domestic Investment
short_term_groups = data.groupby('14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?')['Domestic Investment Percentage'].apply(list)
anova_short_term = f_oneway(*short_term_groups)

# ANOVA: Long-Term Domestic Outlook and Domestic Investment
long_term_groups = data.groupby('15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?')['Domestic Investment Percentage'].apply(list)
anova_long_term = f_oneway(*long_term_groups)

# Regression Analysis: Domestic Outlook on Domestic Investment
X_h2 = data[['14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?', '15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?']]
X_h2 = sm.add_constant(X_h2)  # Add constant for intercept
y_h2 = data['Domestic Investment Percentage']

# Fit the OLS regression model
model_h2 = sm.OLS(y_h2, X_h2).fit()

# Display Results
print("H2: Familiarity Bias and Domestic Investments\n")

# ANOVA Results
print("ANOVA Results - Short-Term Domestic Outlook:")
print(f"F-Statistic: {anova_short_term.statistic:.4f}, P-value: {anova_short_term.pvalue:.4f}")

print("\nANOVA Results - Long-Term Domestic Outlook:")
print(f"F-Statistic: {anova_long_term.statistic:.4f}, P-value: {anova_long_term.pvalue:.4f}")

# Regression Summary
print("\nRegression Summary:")
print(model_h2.summary())