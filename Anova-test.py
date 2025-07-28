# Import required libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare mock dataset: brand perception scores by religious group
data = {
    # Three perception variables repeated for each group
    "Variable": ["Brand Trust", "Loss of Trust", "Negative Perception"] * 4,

    # Group labels (each group appears 3 times for the 3 variables)
    "Group": (
        ["Religious"] * 3
        + ["Traditional"] * 3
        + ["Secular"] * 3
        + ["Other"] * 3
    ),

    # Mean scores for each group-variable combination
    "Mean": [
        2.9, 3.6, 3.9,  # Religious group
        3.0, 3.4, 3.7,  # Traditional group
        3.2, 3.2, 3.5,  # Secular group
        3.1, 3.3, 3.6   # Other group
    ],

    # Standard deviations (used for error bars)
    "Std": [
        0.4, 0.5, 0.5,  # Religious group
        0.3, 0.4, 0.4,  # Traditional group
        0.3, 0.3, 0.3,  # Secular group
        0.2, 0.3, 0.3   # Other group
    ]
}

# Convert the data dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create the base figure for the bar plot
plt.figure(figsize=(10, 6))

# Create a grouped bar plot showing mean scores by variable and group
ax = sns.barplot(
    x="Variable",
    y="Mean",
    hue="Group",
    data=df,
    palette="pastel"
)

# Define order of groups for consistent horizontal offsetting
group_order = ["Religious", "Traditional", "Secular", "Other"]

# Manually add error bars (standard deviation) to each bar
for i, row in df.iterrows():
    # Determine x-axis base index for the current variable
    x_base = ["Brand Trust", "Loss of Trust", "Negative Perception"].index(row["Variable"])
    
    # Calculate horizontal offset to align error bars with the grouped bars
    offset = -0.3 + 0.2 * group_order.index(row["Group"])
    
    # Add vertical error bar
    plt.errorbar(
        x=x_base + offset,       # Adjusted x position
        y=row["Mean"],           # Mean value (height of the bar)
        yerr=row["Std"],         # Error bar length (± std)
        fmt='none',              # No marker
        c='black',               # Color of the error bar
        capsize=5                # Add caps at the ends
    )

# Add plot title and labels
plt.title("Mean Scores by Religious Affiliation – Brand Perception Dimensions")
plt.ylabel("Mean Score")
plt.xlabel("Brand Perception Variable")
plt.ylim(0, 5)  # Set y-axis range

# Show legend
plt.legend(title="Religious Group")

# Optimize layout
plt.tight_layout()

# Display the final plot
plt.show()
