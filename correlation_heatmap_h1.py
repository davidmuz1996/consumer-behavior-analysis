import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from scipy.stats import spearmanr

# Set general English font
matplotlib.rcParams['font.family'] = 'Arial'

# Load Excel file
file_path = "data base.xlsx"
df = pd.read_excel(file_path)

# Define mapping from Hebrew columns to English labels
columns_map = {
    "Sexual": ".פרסומות עם מסרים מיניים בוטים נתפסות בעיניי כפוגעניות",
    "Violence": ".פרסומות עם דימויים אלימים נתפסות בעיניי כפוגעניות",
    "Stereotypes": ".פרסומות המבוססות על סטריאוטיפים מגדריים או גזעיים נתפסות בעיניי כפוגעניות",
    "Religious": ".פרסומות הפוגעות בערכים דתיים נתפסות בעיניי כפוגעניות",
    "Humor": ".פרסומות המשתמשות בהומור ציני או שחור נתפסות בעיניי כפוגעניות",
    "Brand Trust": "?עד כמה את/ה סומכ/ת על מותג שמשתמש במסרים פרובוקטיביים או שנויים במחלוקת בפרסום",
    "Brand Distrust": "?עד כמה פרסומת פוגענית עלולה לגרום לך לאבד אמון במותג"
}

# Select and rename columns
df_selected = df[list(columns_map.values())].rename(columns={v: k for k, v in columns_map.items()})
df_selected = df_selected.dropna()
df_selected = df_selected.apply(pd.to_numeric, errors='coerce')

# Plot correlation heatmap
corr_matrix = df_selected.corr(method='spearman')
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r', center=0, fmt=".2f",
            cbar_kws={'label': 'Spearman Correlation'})
plt.title("Spearman Correlation: Perceived Offensiveness vs Brand Trust", fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# Create r and p-value table
results = []

offensive_types = ["Sexual", "Violence", "Stereotypes", "Religious", "Humor"]
for offensive in offensive_types:
    # r & p with Brand Trust
    r1, p1 = spearmanr(df_selected[offensive], df_selected["Brand Trust"])
    # r & p with Brand Distrust
    r2, p2 = spearmanr(df_selected[offensive], df_selected["Brand Distrust"])
    results.append({
        "Type of Offensiveness": offensive,
        "Trust in Brand (r)": round(r1, 2),
        "Trust in Brand (p)": round(p1, 4),
        "Loss of Trust (r)": round(r2, 2),
        "Loss of Trust (p)": round(p2, 4),
    })

# Create DataFrame
correlation_df = pd.DataFrame(results)

# Print the table
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)
pd.set_option('display.max_colwidth', None)

print("\nSpearman r and p-values Table:")
print(correlation_df)
