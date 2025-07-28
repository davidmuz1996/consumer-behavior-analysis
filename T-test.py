# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------------------------------------------
# Create a DataFrame with mean scores and standard errors
# for three perception variables, split by gender (Male/Female)
# -------------------------------------------------------
plot_data = pd.DataFrame({
    "Variable": ["Trust", "Trust", "Trust Loss", "Trust Loss", "Negative Perception", "Negative Perception"],
    "Group": ["Male", "Female"] * 3,  # Alternating gender labels
    "Mean": [3.2, 3.4, 3.5, 3.7, 3.8, 4.1],  # Mean scores for each group
    "SE": [0.2, 0.25, 0.23, 0.21, 0.22, 0.24]  # Standard error for each bar
})

# -------------------------------------------------------
# Create the base bar plot
# -------------------------------------------------------
plt.figure(figsize=(8, 5))  # Set the figure size

# Draw bar plot grouped by "Group" (Male/Female) for each variable
ax = sns.barplot(
    x="Variable",      # X-axis: perception variable
    y="Mean",          # Y-axis: mean score
    hue="Group",       # Grouping by gender
    data=plot_data,
    palette="pastel"   # Use light color palette
)

# -------------------------------------------------------
# Add error bars manually to each bar using standard error
# -------------------------------------------------------
for index, row in plot_data.iterrows():
    # Compute the x-position adjustment to align error bars with bars
    # Bars are grouped, so we offset left/right based on gender
    ax.errorbar(
        x=index % 3 + (-0.2 if row['Group'] == 'Male' else 0.2),  # Adjust x-position
        y=row['Mean'],              # Bar height (mean score)
        yerr=row['SE'],             # Length of error bar (± standard error)
        fmt='none',                 # No marker
        c='black',                  # Error bar color
        capsize=5                   # Add caps at the ends of the error bars
    )

# -------------------------------------------------------
# Add labels and formatting
# -------------------------------------------------------
plt.title("T-Test Group Comparison by Gender")         # Plot title
plt.ylabel("Mean Score")                               # Label for y-axis
plt.xlabel("Variable")                                 # Label for x-axis
plt.legend(title="Group")                              # Legend title
plt.tight_layout()                                     # Adjust layout to avoid overlap

# -------------------------------------------------------
# Display the final plot
# -------------------------------------------------------
plt.show()
