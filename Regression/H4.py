import pandas as pd
import statsmodels.api as sm
from scipy.stats import pearsonr

# Load your dataset
data = pd.read_excel('survey_answers.xlsx'')

# Rename columns for clarity (if needed)
data = data.rename(columns={
    '18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?': 'Percentage of Foreign Assets',
    '14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?': 'Short-Term Domestic Outlook',
    '15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?': 'Long-Term Domestic Outlook'
})

# Drop rows with missing data in relevant columns
data = data.dropna(subset=['Short-Term Domestic Outlook', 'Long-Term Domestic Outlook', 'Percentage of Foreign Assets'])

# H4.1: Correlation Analysis
# Correlation between short-term domestic outlook and foreign investments
corr_short, pval_short = pearsonr(data['Short-Term Domestic Outlook'], data['Percentage of Foreign Assets'])

# Correlation between long-term domestic outlook and foreign investments
corr_long, pval_long = pearsonr(data['Long-Term Domestic Outlook'], data['Percentage of Foreign Assets'])

# H4.2: Regression Analysis
X_h4 = data[['Short-Term Domestic Outlook', 'Long-Term Domestic Outlook']]
X_h4 = sm.add_constant(X_h4)  # Add constant for intercept
y_h4 = data['Percentage of Foreign Assets']

# Fit the OLS regression model
model_h4 = sm.OLS(y_h4, X_h4).fit()

# Display Results
print("H4: Domestic Economic Outlook and Home Bias\n")
print("Correlation Analysis:")
print(f"Short-Term Outlook - Correlation: {corr_short:.4f}, P-value: {pval_short:.4f}")
print(f"Long-Term Outlook - Correlation: {corr_long:.4f}, P-value: {pval_long:.4f}")

print("\nRegression Summary:")
print(model_h4.summary())
