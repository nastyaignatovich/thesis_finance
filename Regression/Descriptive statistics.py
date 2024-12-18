import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
with open("../Regression/data.pkl", 'rb') as f:
    data = pickle.load(f)

# Calculate descriptive statistics
desc_stats = data.agg(['count', 'mean', 'std', 'min', 'max']).round(3)
desc_stats = desc_stats.T  # Transpose for better readability
desc_stats.columns = ['N', 'Mean', 'Std.Dev', 'Min', 'Max']
desc_stats.to_excel('descriptive_statistics.xlsx')  # Save to Excel for reference

# Set global font size for figures
plt.rcParams.update({'font.size': 12})

# Visualization of means (Figure 1)
plt.figure(figsize=(10, 6))
plt.barh(desc_stats.index, desc_stats['Mean'], color='skyblue')
plt.xlabel('Mean Value')
plt.tight_layout()
plt.savefig('Figure_1_Mean_Values.png', dpi=300, bbox_inches='tight')
plt.show()

# Visualization of standard deviations (Figure 2)
plt.figure(figsize=(10, 6))
plt.barh(desc_stats.index, desc_stats['Std.Dev'], color='salmon')
plt.xlabel('Standard Deviation')
plt.tight_layout()
plt.savefig('Figure_2_Standard_Deviations.png', dpi=300, bbox_inches='tight')
plt.show()

# Histogram for Foreign Portfolio Allocation (Figure 3)
plt.figure(figsize=(8, 6))
data['foreign_portfolio_pct'].plot(kind='hist', bins=20, color='skyblue', alpha=0.7)
plt.xlabel('Percentage of Portfolio Invested Abroad')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('Figure_3_Foreign_Portfolio_Distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Histogram for Expected Returns (Figure 4)
plt.figure(figsize=(8, 6))
data['expected_return'].plot(kind='hist', bins=15, color='purple', alpha=0.7)
plt.xlabel('Expected Return (%)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('Figure_4_Expected_Returns_Distribution.png', dpi=300, bbox_inches='tight')
plt.show()

print("Visualizations created and saved as 'Figure_1_Mean_Values.png', 'Figure_2_Standard_Deviations.png', 'Figure_3_Foreign_Portfolio_Distribution.png', and 'Figure_4_Expected_Returns_Distribution.png'.")
