import pandas as pd
import pickle

# File pathsr"C
input_path = "../Regression/data.pkl"
output_path = "../Regression/data.pkl"

# Load the original data
print("Loading original data...")
with open(input_path, 'rb') as f:
    data = pickle.load(f)

# Print original columns
print("\nOriginal columns:")
print(data.columns.tolist())

# Create new variables
data['domestic_outlook_diff'] = data['domestic_outlook_long'] - data['domestic_outlook_short']
data['global_outlook_diff'] = data['global_outlook_long'] - data['global_outlook_short']
data['short_outlook_diff'] = data['global_outlook_short'] - data['domestic_outlook_short']
data['long_outlook_diff'] = data['global_outlook_long'] - data['domestic_outlook_long']

# Save the updated dataset
print("\nSaving updated data...")
with open(output_path, 'wb') as f:
    pickle.dump(data, f)

# Verify the save worked by loading the new file
print("\nVerifying saved data...")
with open(output_path, 'rb') as f:
    verified_data = pickle.load(f)

# Print new columns
print("\nNew columns in saved data:")
print(verified_data.columns.tolist())

# Print sample of new variables
print("\nSample of new variables (first 5 rows):")
print(verified_data[['domestic_outlook_diff', 'global_outlook_diff',
                    'short_outlook_diff', 'long_outlook_diff']].head())