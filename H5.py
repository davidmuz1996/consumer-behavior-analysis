# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------
# Create a DataFrame with summary data
# ---------------------------------------------
df_table5 = pd.DataFrame({
    "Brand Type": ["Offensive Brand", "Other Brands in the Same Category"],
    "Mean": [3.91, 3.13],  # Average perception score
    "Standard Deviation": [0.96, 1.09]  # Corresponding standard deviations
})

# Print the data (optional for debugging or preview)
print(df_table5)

# ---------------------------------------------
# Set up the bar plot
# ---------------------------------------------
plt.figure(figsize=(7, 5))  # Define plot size

# Create barplot using seaborn
ax = sns.barplot(
    x="Brand Type",          # X-axis categories
    y="Mean",                # Y-axis values
    hue="Brand Type",        # Use brand type for coloring (not really necessary here, but safe)
    data=df_table5,
    palette="pastel",        # Soft colors
    edgecolor=".2",          # Border color for bars
    legend=False             # Disable legend to avoid redundancy (hue and x are the same)
)

# ---------------------------------------------
# Manually add error bars (standard deviation)
# ---------------------------------------------
for i, row in df_table5.iterrows():
    ax.errorbar(
        x=i,                         # Bar position on x-axis
        y=row["Mean"],              # Height of the bar (mean score)
        yerr=row["Standard Deviation"],  # Length of the error bar
        fmt='none',                 # No data point marker
        c='black',                  # Color of error bars
        capsize=5                   # Size of the caps at the ends of error bars
    )

# ---------------------------------------------
# Final plot formatting
# ---------------------------------------------
ax.set_title("Negative perceptions of the offensive brand vs. other brands in the same category")
ax.set_ylabel("Mean Negative Perception")  # Label for y-axis
ax.set_xlabel("")                          # Empty x-axis label

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()
