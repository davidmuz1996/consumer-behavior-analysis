# -------------------------------------------------------
# Import necessary libraries
# -------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -------------------------------------------------------
# Define correlation results between moral sensitivity
# and brand perception dimensions
# -------------------------------------------------------
data = {
    "Variable": [
        "Trust in Brand",
        "Loss of Trust",
        "Negative Brand Perception"
    ],
    "Spearman Correlation (r)": [-0.18, 0.26, 0.33],  # Spearman correlation coefficients
    "p-value": [0.021, 0.001, 0.000]                  # Statistical significance
}

# -------------------------------------------------------
# Create a DataFrame to store and display the correlation results
# -------------------------------------------------------
df = pd.DataFrame(data)
print(df)  # Print the correlation and p-values table

# -------------------------------------------------------
# Prepare data for the heatmap
# -------------------------------------------------------
# Dictionary with correlation values only (used for visualization)
data = {
    "Trust in Brand": [-0.18],
    "Loss of Trust": [0.26],
    "Negative Perception": [0.33]
}

# Create DataFrame with "Moral Sensitivity" as index row
df = pd.DataFrame(data, index=["Moral Sensitivity"])

# -------------------------------------------------------
# Create a heatmap to visualize the correlations
# -------------------------------------------------------
plt.figure(figsize=(8, 2))  # Set figure size (wide and short layout)

# Draw heatmap with annotations, diverging color scale
sns.heatmap(
    df,
    annot=True,                     # Show correlation values inside cells
    cmap="RdBu_r",                  # Diverging color map (red to blue)
    center=0,                       # Centered around 0 for better contrast
    cbar_kws={'label': 'Spearman Correlation'}  # Color bar label
)

# Add title and format y-axis labels
plt.title("Spearman Correlation – Moral Sensitivity vs. Brand Perception")
plt.yticks(rotation=0)  # Keep y-axis labels horizontal
plt.tight_layout()      # Adjust spacing to fit layout

# Show the final heatmap
plt.show()
