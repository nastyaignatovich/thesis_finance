import pandas as pd
import statsmodels.api as sm
from scipy.stats import f_oneway

# Load your dataset
data = pd.read_excel('survey_answers.xlsx'')

# Rename columns for clarity (if needed)
data = data.rename(columns={
    '18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?': 'Percentage of Foreign Assets',
    '14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?': 'Short-Term Domestic Outlook',
    '15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?': 'Long-Term Domestic Outlook'
})

# Calculate Domestic Investment Percentage
data['Domestic Investment Percentage'] = 100 - data['Percentage of Foreign Assets']

# Drop rows with missing values in relevant columns
data = data.dropna(subset=['Short-Term Domestic Outlook', 'Long-Term Domestic Outlook', 'Domestic Investment Percentage'])

# Group data for ANOVA
short_term_groups = data.groupby('Short-Term Domestic Outlook')['Domestic Investment Percentage'].apply(list)
long_term_groups = data.groupby('Long-Term Domestic Outlook')['Domestic Investment Percentage'].apply(list)

# Perform ANOVA
anova_short_term = f_oneway(*short_term_groups)
anova_long_term = f_oneway(*long_term_groups)

# Regression Analysis
X_h2 = data[['Short-Term Domestic Outlook', 'Long-Term Domestic Outlook']]
X_h2 = sm.add_constant(X_h2)  # Add constant for intercept
y_h2 = data['Domestic Investment Percentage']

# Fit the OLS regression model
model_h2 = sm.OLS(y_h2, X_h2).fit()

# Display Results
print("H2: Familiarity Bias and Domestic Investments\n")
print("ANOVA Results - Short-Term Domestic Outlook:")
print(f"F-Statistic: {anova_short_term.statistic:.4f}, P-value: {anova_short_term.pvalue:.4f}")

print("\nANOVA Results - Long-Term Domestic Outlook:")
print(f"F-Statistic: {anova_long_term.statistic:.4f}, P-value: {anova_long_term.pvalue:.4f}")

print("\nLinear Regression Summary:")
print(model_h2.summary())
