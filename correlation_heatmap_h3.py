# -------------------------------------------------------
# Import necessary libraries
# -------------------------------------------------------
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Define labels for offensive message types and consumer responses
# -------------------------------------------------------
offensive_types = [
    "Sexual Content",
    "Violent Imagery",
    "Stereotypes (Gender/Race)",
    "Religious Offense",
    "Cynical/Dark Humor"
]

reaction_vars = [
    "Stopped Buying",         # Whether the consumer stopped buying from the brand
    "Social Media Role",      # Importance of social media in raising awareness
    "Public Reaction Intent"  # Intention to react publicly (e.g., boycott, post)
]

# -------------------------------------------------------
# Generate mock Spearman correlation values and p-values
# -------------------------------------------------------
np.random.seed(42)  # Set seed for reproducibility

# Random correlation coefficients between -0.1 and 0.5
r_values = np.random.uniform(low=-0.1, high=0.5, size=(5, 3))

# Random p-values between 0.001 and 0.2
p_values = np.random.uniform(low=0.001, high=0.2, size=(5, 3))

# Round the values for readability
r_values = np.round(r_values, 2)
p_values = np.round(p_values, 3)

# -------------------------------------------------------
# Create a combined table of correlation results
# -------------------------------------------------------
rows = []
for i, offensive in enumerate(offensive_types):
    for j, reaction in enumerate(reaction_vars):
        rows.append({
            "Offensive Message Type": offensive,
            "Reaction Variable": reaction,
            "Spearman r": r_values[i][j],     # Correlation coefficient
            "p-value": p_values[i][j]         # Statistical significance
        })

# Convert the results into a DataFrame
df_corr = pd.DataFrame(rows)

# Print the full correlation table
print(df_corr)

# -------------------------------------------------------
# Create a simplified correlation matrix for heatmap display
# (Using custom static values for illustrative clarity)
# -------------------------------------------------------
data = {
    'Stopped Buying':       [-0.05, 0.24, 0.12, -0.08, 0.11],
    'Social Media Role':    [0.39, 0.35, 0.31, 0.04, 0.22],
    'Public Reaction Intent': [0.43, 0.17, 0.29, -0.03, 0.19]
}

# Use offensive message types as row labels (index)
index = ['Violent Content', 'Cynical Humor', 'Stereotypes', 'Religious Offense', 'Sexual Content']

# Create DataFrame for heatmap
df = pd.DataFrame(data, index=index)

# -------------------------------------------------------
# Plot heatmap of correlations
# -------------------------------------------------------
plt.figure(figsize=(10, 6))  # Set figure size

sns.heatmap(
    df,
    annot=True,           # Show correlation values inside the heatmap
    cmap='RdBu_r',        # Diverging color map: red = negative, blue = positive
    center=0              # Center color scale around zero
)

# Add titles and labels
plt.title('Spearman Correlations between Perceived Offensive Messages and Consumer Reactions')
plt.xlabel('Consumer Response Variable')
plt.ylabel('Type of Offensive Message')
plt.tight_layout()  # Adjust layout to prevent overlap

# Show the plot
plt.show()
