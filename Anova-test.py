# Fixing the error by removing the unsupported `errorbar` argument in seaborn version
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for demonstration (replace with real means and stds if available)
data = {
    "Variable": ["Brand Trust", "Loss of Trust", "Negative Perception"] * 4,
    "Group": (
        ["Religious"] * 3
        + ["Traditional"] * 3
        + ["Secular"] * 3
        + ["Other"] * 3
    ),
    "Mean": [
        2.9, 3.6, 3.9,  # Religious
        3.0, 3.4, 3.7,  # Traditional
        3.2, 3.2, 3.5,  # Secular
        3.1, 3.3, 3.6   # Other
    ],
    "Std": [
        0.4, 0.5, 0.5,  # Religious
        0.3, 0.4, 0.4,  # Traditional
        0.3, 0.3, 0.3,  # Secular
        0.2, 0.3, 0.3   # Other
    ]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))
ax = sns.barplot(x="Variable", y="Mean", hue="Group", data=df, palette="pastel")

# Add error bars manually
group_order = ["Religious", "Traditional", "Secular", "Other"]
for i, row in df.iterrows():
    x_base = ["Brand Trust", "Loss of Trust", "Negative Perception"].index(row["Variable"])
    offset = -0.3 + 0.2 * group_order.index(row["Group"])
    plt.errorbar(
        x=x_base + offset,
        y=row["Mean"],
        yerr=row["Std"],
        fmt='none',
        c='black',
        capsize=5
    )

plt.title("Mean Scores by Religious Affiliation – Brand Perception Dimensions")
plt.ylabel("Mean Score")
plt.xlabel("Brand Perception Variable")
plt.ylim(0, 5)
plt.legend(title="Religious Group")
plt.tight_layout()
plt.show()
