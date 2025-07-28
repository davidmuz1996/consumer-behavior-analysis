import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

# Example data for Table 6
# Perceived trust in offending brand vs trust in similar brands
data = {
    "Trust_Offending_Brand": [2, 3, 1, 4, 2, 3, 2, 1, 4, 3],
    "Trust_Similar_Brands": [3, 3, 2, 4, 3, 2, 3, 2, 4, 3]
}

df = pd.DataFrame(data)

# Calculate Spearman correlation
corr, p_value = spearmanr(df["Trust_Offending_Brand"], df["Trust_Similar_Brands"])

# Prepare Table 6
table6 = pd.DataFrame({
    "Variable 1": ["Trust in Offending Brand"],
    "Variable 2": ["Trust in Similar Brands"],
    "Spearman Correlation": [round(corr, 2)],
    "p-value": [round(p_value, 3)]
})

# Display Table 6
# Display full Table 6
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
print(table6)
# Plot Figure 7 - Scatter plot with trend line
plt.figure(figsize=(6, 4))
sns.regplot(x="Trust_Offending_Brand", y="Trust_Similar_Brands", data=df,
            scatter_kws={"s": 50}, line_kws={"color": "red"}, ci=None)
plt.title("Spearman Correlation - Trust in Offending vs Similar Brands")
plt.xlabel("Trust in Offending Brand")
plt.ylabel("Trust in Similar Brands")
plt.grid(True)
plt.tight_layout()
plt.show()
