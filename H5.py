import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
df_table5 = pd.DataFrame({
    "Brand Type": ["Offensive Brand", "Other Brands in the Same Category"],
    "Mean": [3.91, 3.13],
    "Standard Deviation": [0.96, 1.09]
})
print(df_table5)

# Set hue = x and disable legend to avoid future warning
plt.figure(figsize=(7, 5))
ax = sns.barplot(
    x="Brand Type",
    y="Mean",
    hue="Brand Type",  # Using the same variable for hue
    data=df_table5,
    palette="pastel",
    edgecolor=".2",
    legend=False       # No need for a duplicate legend
)

# Add error bars
for i, row in df_table5.iterrows():
    ax.errorbar(
        x=i,
        y=row["Mean"],
        yerr=row["Standard Deviation"],
        fmt='none',
        c='black',
        capsize=5
    )

# Labels and title
ax.set_title("Negative perceptions of the offensive brand vs. other "
             "brands in the same category")
ax.set_ylabel("Mean Negative Perception")
ax.set_xlabel("")
plt.tight_layout()
plt.show()
