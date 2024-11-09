import pandas as pd
import matplotlib.pyplot as plt
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '../data/nvdrs-data-export.csv')

# Normalize the path to remove any redundant separators
file_path = os.path.normpath(file_path)

# Load the data from CSV file
data = pd.read_csv(file_path)

# Optional: Display the first few rows to verify the data is loaded correctly
print(data.head())

# Create the output directory if it doesn't exist
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Clean and Convert 'Death Count' and 'Population' columns
data['Death Count'] = data['Death Count'].fillna('0').replace(',', '', regex=True).astype(int)
data['Population'] = data['Population'].fillna('0').replace(',', '', regex=True).astype(int)

# Ensure 'Intent or Manner' column is string and fill NaNs with "Unknown"
data['Intent or Manner'] = data['Intent or Manner'].fillna("Unknown").astype(str)

# 2. Calculate the Percentage of Each Death Count
data['Death Percentage'] = (data['Death Count'] / data['Death Count'].sum()) * 100

# 3. Visualize Death Count by Intent or Manner and save as an image
plt.figure(figsize=(10, 6))
plt.bar(data['Intent or Manner'], data['Death Count'], color='skyblue')
plt.title('Death Counts by Intent or Manner')
plt.xlabel('Intent or Manner')
plt.ylabel('Death Count')
plt.savefig(f'{output_dir}/death_counts_by_intent.png')  # Save the plot as an image in the output directory
plt.close()  # Close the figure to free memory

# 4. Visualize the Proportion of Deaths by Intent as a Pie Chart and save as an image
plt.figure(figsize=(8, 8))
plt.pie(data['Death Percentage'], labels=data['Intent or Manner'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Deaths by Intent or Manner')
plt.savefig(f'{output_dir}/death_proportion_by_intent.png')  # Save the plot as an image in the output directory
plt.close()

# 5. Compare Crude Rate and Age-Adjusted Rate by Intent and save as an image
data.plot(x='Intent or Manner', y=['Crude Rate', 'Age Adjusted Rate'], kind='bar', figsize=(10, 6))
plt.title('Crude Rate vs Age-Adjusted Rate by Intent or Manner')
plt.xlabel('Intent or Manner')
plt.ylabel('Rate per 100,000')
plt.savefig(f'{output_dir}/rate_comparison_by_intent.png')  # Save the plot as an image in the output directory
plt.close()

print(f"Plots have been saved in the '{output_dir}' directory.")
