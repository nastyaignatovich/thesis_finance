import pandas as pd
import pickle

# Load the data
with open("../Regression/data.pkl", "rb") as f:
    data = pickle.load(f)

# Create a dictionary for column renaming
new_names = {
    '1. What is your age?\n': 'age',
    '2. What is your gender? ': 'gender',
    '3. What is your marital status?': 'marital',
    '4. What is your highest level of education?': 'education',
    '5. Is your current occupation related to STEM fields?': 'stem_job',
    '6. Is your current occupation related to economics and/or finance?': 'finance_job',
    '7. How many years of professional experience do you have?': 'experience',
    '8. What is your annual income in EUR after taxes? ': 'income',
    '9. If you stopped working today and liquidated all your assets (both financial and real estate), for how many months could you maintain your current lifestyle and spending habits? ': 'savings_months',
    '10. How would you rate your financial literacy?': 'fin_literacy',
    '11. How confident are you in your investment decisions?': 'invest_confidence',
    '12. How would you rate your risk tolerance?': 'risk_tolerance',
    '13. What is your typical investment horizon?': 'invest_horizon',
    '14. How do you view the short-term (next 1–2 years) economic outlook for your home country (where you reside and work)?': 'domestic_outlook_short',
    '15. How do you view the long-term (next 5–10 years) economic outlook for your home country (where you reside and work)?': 'domestic_outlook_long',
    '16. How do you view the short-term (next 1–2 years) economic outlook for the global economy?': 'global_outlook_short',
    '17. How do you view the long-term (next 5–10 years) economic outlook for the global economy?': 'global_outlook_long',
    '18. What percentage of your financial portfolio (stocks, bonds, ETFs, investment funds) is invested in assets outside your home country?': 'foreign_portfolio_pct',
    '19. What percentage of your entire assets (real estate, financial assets including cryptocurrency and other instruments, and other assets) is invested in assets outside your home country? ': 'foreign_assets_pct',
    '20. How important are investment fees when choosing investments?': 'fee_importance',
    '21. What is your annual expected rate of return on your investments?': 'expected_return'
}

# Rename the columns
data = data.rename(columns=new_names)

# Save the updated DataFrame back to pickle
with open("../Regression/data.pkl", "wb") as f:
    pickle.dump(data, f)

# Print the new column names to verify
print("New column names:")
for i, col in enumerate(data.columns, 1):
    print(f"{i}. {col}")