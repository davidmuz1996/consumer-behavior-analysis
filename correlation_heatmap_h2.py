import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import matplotlib

# Set font to Arial to avoid issues with Hebrew display
matplotlib.rcParams['font.family'] = 'Arial'

# Load the Excel file
file_path = "data base.xlsx"
df = pd.read_excel(file_path)

# Define the mapping of relevant questions to English column names
columns_map = {
    "Sexual": ".פרסומות עם מסרים מיניים בוטים נתפסות בעיניי כפוגעניות",
    "Violence": ".פרסומות עם דימויים אלימים נתפסות בעיניי כפוגעניות",
    "Stereotypes": ".פרסומות המבוססות על סטריאוטיפים מגדריים או גזעיים נתפסות בעיניי כפוגעניות",
    "Religious": ".פרסומות הפוגעות בערכים דתיים נתפסות בעיניי כפוגעניות",
    "Humor": ".פרסומות המשתמשות בהומור ציני או שחור נתפסות בעיניי כפוגעניות",
    "Purchase Intention": "?האם פרסומת פוגענית תשפיע על החלטתך לרכוש ממותג זה בעתיד",
    "Past Avoidance": "?האם יצא לך להפסיק לרכוש ממותג בעקבות מסר פרסומי פוגעני"
}

# Select and rename columns
df_selected = df[list(columns_map.values())].rename(columns={v: k for k, v in columns_map.items()})
df_selected = df_selected.dropna()
df_selected = df_selected.apply(pd.to_numeric, errors='coerce')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

# Compute Spearman correlations and p-values
offensiveness = ["Sexual", "Violence", "Stereotypes", "Religious", "Humor"]
outcomes = ["Purchase Intention", "Past Avoidance"]
results = []

for offensive in offensiveness:
    row = {"Type of Offensiveness": offensive}
    for outcome in outcomes:
        r, p = spearmanr(df_selected[offensive], df_selected[outcome])
        row[f"{outcome} (r)"] = round(r, 2)
        row[f"{outcome} (p)"] = round(p, 4)
    results.append(row)

results_df = pd.DataFrame(results)

# Display the full table
print("\nSpearman Correlation Table for H2:")
print(results_df)

# Create heatmap
plt.figure(figsize=(8, 6))
heatmap_data = df_selected.corr(method='spearman').loc[offensiveness, outcomes]
sns.heatmap(heatmap_data, annot=True, cmap='RdBu', center=0, fmt=".2f", cbar_kws={'label': 'Spearman Correlation'})
plt.title("Spearman Correlation: Perceived Offensiveness vs Consumer Loyalty", fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
