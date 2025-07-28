# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

# -------------------------------------------------------
# Sample data: Trust ratings for two types of brands
# -------------------------------------------------------
data = {
    "Trust_Offending_Brand": [2, 3, 1, 4, 2, 3, 2, 1, 4, 3],  # Trust in a brand that used offensive advertising
    "Trust_Similar_Brands": [3, 3, 2, 4, 3, 2, 3, 2, 4, 3]   # Trust in other brands in the same category
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# -------------------------------------------------------
# Calculate Spearman correlation between the two trust scores
# -------------------------------------------------------
corr, p_value = spearmanr(df["Trust_Offending_Brand"], df["Trust_Similar_Brands"])

# -------------------------------------------------------
# Create a summary table (Table 6) showing correlation results
# -------------------------------------------------------
table6 = pd.DataFrame({
    "Variable 1": ["Trust in Offending Brand"],
    "Variable 2": ["Trust in Similar Brands"],
    "Spearman Correlation": [round(corr, 2)],  # Rounded correlation coefficient
    "p-value": [round(p_value, 3)]            # Rounded p-value
})

# -------------------------------------------------------
# Print the correlation results table
# -------------------------------------------------------
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
print(table6)

# -------------------------------------------------------
# Plot the relationship as a scatter plot with regression line
# -------------------------------------------------------
plt.figure(figsize=(6, 4))

# Create scatter plot with trend line using seaborn
sns.regplot(
    x="Trust_Offending_Brand",
    y="Trust_Similar_Brands",
    data=df,
    scatter_kws={"s": 50},        # Marker size
    line_kws={"color": "red"},    # Regression line color
    ci=None                       # No confidence interval shading
)

# Add titles and axis labels
plt.title("Spearman Correlation - Trust in Offending vs Similar Brands")
plt.xlabel("Trust in Offending Brand")
plt.ylabel("Trust in Similar Brands")
plt.grid(True)           # Add background grid
plt.tight_layout()       # Avoid layout overlap

# Show the final plot
plt.show()
