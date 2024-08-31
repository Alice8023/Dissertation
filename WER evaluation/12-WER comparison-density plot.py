import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import os

# Read the WER08062.csv file
wer_08062_df = pd.read_csv("WER08062.csv")

# Ensure the WER column is numeric
wer_08062_df['WER'] = pd.to_numeric(wer_08062_df['WER'], errors='coerce')

# Remove rows containing NaN in the WER column
wer_08062_df = wer_08062_df.dropna(subset=['WER'])

# Filter out WER values greater than 1
wer_08062_df = wer_08062_df[wer_08062_df['WER'] <= 1]

# Set the plotting style
sns.set(style="whitegrid")

# Create a larger figure
plt.figure(figsize=(10, 6))

# Calculate density estimation
data = wer_08062_df['WER']
kde = gaussian_kde(data, bw_method='scott')
x = np.linspace(0, 1, 1000)  # Define the range for the x-axis
kde_values = kde.evaluate(x)

# Plot the density graph
sns.kdeplot(data=data, fill=True, color='blue', linewidth=2, alpha=0.6)

# Find the peak point
max_idx = np.argmax(kde_values)
peak_x = x[max_idx]
peak_y = kde_values[max_idx]

# Annotate the peak point
plt.text(peak_x, peak_y, f'Peak: ({peak_x:.2f}, {peak_y:.2f})',
         horizontalalignment='center',
         verticalalignment='bottom',
         fontsize=12,
         color='red',
         bbox=dict(facecolor='none', edgecolor='none'))

# Add labels and title
plt.xlabel('WER', fontsize=14)
plt.ylabel('Density', fontsize=14)

# Specify the folder path to save the plot
output_folder = "plots"

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Specify the file name to save the plot
output_path = os.path.join(output_folder, "density_plot_wer08062_with_peak2.png")

# Save the plot
plt.savefig(output_path, bbox_inches='tight')

# Display the plot
plt.show()
