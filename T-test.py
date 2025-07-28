import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# הנתונים
plot_data = pd.DataFrame({
    "Variable": ["Trust", "Trust", "Trust Loss", "Trust Loss", "Negative Perception", "Negative Perception"],
    "Group": ["Male", "Female"] * 3,
    "Mean": [3.2, 3.4, 3.5, 3.7, 3.8, 4.1],
    "SE": [0.2, 0.25, 0.23, 0.21, 0.22, 0.24]
})

plt.figure(figsize=(8, 5))
ax = sns.barplot(x="Variable", y="Mean", hue="Group", data=plot_data, palette="pastel")

# הוספת שגיאה באמצעות error bars
for index, row in plot_data.iterrows():
    ax.errorbar(
        x=index % 3 + (-0.2 if row['Group'] == 'Male' else 0.2),
        y=row['Mean'],
        yerr=row['SE'],
        fmt='none',
        c='black',
        capsize=5
    )

plt.title("T-Test Group Comparison by Gender")
plt.ylabel("Mean Score")
plt.xlabel("Variable")
plt.legend(title="Group")
plt.tight_layout()
plt.show()
