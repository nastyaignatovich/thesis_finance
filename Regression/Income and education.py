import pandas as pd
import pickle

# File paths
input_path = "../Regression/data.pkl"
output_path = "../Regression/data.pkl"
# Load the data
print("Loading data...")
with open(input_path, 'rb') as f:
    data = pickle.load(f)

# Create binary variables
print("\nCreating binary variables...")

# Education binary (1 if education >= 1, 0 otherwise)
data['education_high'] = (data['education'] >= 1).astype(int)

# Income medium (1 if income = 1, 0 otherwise)
data['income_medium'] = (data['income'] == 1).astype(int)

# Income high (1 if income = 2 or 3, 0 otherwise)
data['income_high'] = (data['income'].isin([2, 3])).astype(int)

# Print verification of new variables
print("\nVerification of new variables:")
print("\nEducation high distribution:")
print(data['education_high'].value_counts())
print("\nIncome medium distribution:")
print(data['income_medium'].value_counts())
print("\nIncome high distribution:")
print(data['income_high'].value_counts())

# Cross-check with original variables
print("\nCross-check with original variables:")
print("\nOriginal education values:")
print(data['education'].value_counts())
print("\nOriginal income values:")
print(data['income'].value_counts())

# Save the updated dataset
print("\nSaving updated data...")
with open(output_path, 'wb') as f:
    pickle.dump(data, f)

# Verify the save worked
print("\nVerifying saved data...")
with open(output_path, 'rb') as f:
    verified_data = pickle.load(f)

# Final verification
print("\nNew variables in saved dataset:")
new_vars = ['education_high', 'income_medium', 'income_high']
for var in new_vars:
    print(f"\n{var} exists in saved data:", var in verified_data.columns)
    if var in verified_data.columns:
        print(f"Distribution of {var}:")
        print(verified_data[var].value_counts())