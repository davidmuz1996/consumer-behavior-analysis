import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# הגדרת הנתונים
data = {
    "Variable": [
        "Trust in Brand",
        "Loss of Trust",
        "Negative Brand Perception"
    ],
    "Spearman Correlation (r)": [-0.18, 0.26, 0.33],
    "p-value": [0.021, 0.001, 0.000]
}

# יצירת DataFrame
df = pd.DataFrame(data)
print(df)


data = {
    "Trust in Brand": [-0.18],
    "Loss of Trust": [0.26],
    "Negative Perception": [0.33]
}
df = pd.DataFrame(data, index=["Moral Sensitivity"])
# הכנה ל-heatmap: נשתמש רק בעמודת הר עבור heatmap

# ציור heatmap
plt.figure(figsize=(8, 2))
sns.heatmap(df, annot=True, cmap="RdBu_r", center=0,
            cbar_kws={'label': 'Spearman Correlation'})
plt.title("Spearman Correlation – Moral Sensitivity vs. Brand Perception")
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
