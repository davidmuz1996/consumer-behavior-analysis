# -------------------------------------------------------
# Import necessary libraries
# -------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import matplotlib

# -------------------------------------------------------
# Set font to Arial to ensure proper display of Hebrew text (if present)
# -------------------------------------------------------
matplotlib.rcParams['font.family'] = 'Arial'

# -------------------------------------------------------
# Load the Excel file containing the survey data
# -------------------------------------------------------
file_path = "data base.xlsx"
df = pd.read_excel(file_path)

# -------------------------------------------------------
# Map Hebrew survey questions to English column names
# -------------------------------------------------------
columns_map = {
    "Sexual": "Advertisements with explicit sexual content are perceived by me as offensive.",
    "Violence": "Advertisements with violent imagery are perceived by me as offensive.",
    "Stereotypes": "Advertisements based on gender or racial stereotypes are perceived by me as offensive.",
    "Religious": "Advertisements that offend religious values are perceived by me as offensive.",
    "Humor": "Advertisements using cynical or dark humor are perceived by me as offensive.",
    "Purchase Intention": "Will an offensive advertisement affect your decision to buy from this brand in the future?",
    "Past Avoidance": "Have you ever stopped buying from a brand because of an offensive advertisement?"
}

# -------------------------------------------------------
# Select only relevant columns, rename them to English,
# remove missing values, and convert all values to numeric
# -------------------------------------------------------
df_selected = df[list(columns_map.values())].rename(columns={v: k for k, v in columns_map.items()})
df_selected = df_selected.dropna()
df_selected = df_selected.apply(pd.to_numeric, errors='coerce')

# Optional: Configure pandas display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

# -------------------------------------------------------
# Compute Spearman correlations between offensiveness and loyalty outcomes
# -------------------------------------------------------
offensiveness = ["Sexual", "Violence", "Stereotypes", "Religious", "Humor"]
outcomes = ["Purchase Intention", "Past Avoidance"]
results = []

# Loop through each combination and compute correlation and p-value
for offensive in offensiveness:
    row = {"Type of Offensiveness": offensive}
    for outcome in outcomes:
        r, p = spearmanr(df_selected[offensive], df_selected[outcome])
        row[f"{outcome} (r)"] = round(r, 2)
        row[f"{outcome} (p)"] = round(p, 4)
    results.append(row)

# Store results in DataFrame
results_df = pd.DataFrame(results)

# -------------------------------------------------------
# Print correlation table to console
# -------------------------------------------------------
print("\nSpearman Correlation Table for H2:")
print(results_df)

# -------------------------------------------------------
# Create a heatmap showing the strength of correlations
# -------------------------------------------------------
plt.figure(figsize=(8, 6))
heatmap_data = df_selected.corr(method='spearman').loc[offensiveness, outcomes]

sns.heatmap(
    heatmap_data,
    annot=True,                # Show values inside cells
    cmap='RdBu',               # Diverging color map
    center=0,                  # Centered around zero
    fmt=".2f",                 # Format to 2 decimal places
    cbar_kws={'label': 'Spearman Correlation'}
)

# Formatting the plot
plt.title("Spearman Correlation: Perceived Offensiveness vs Consumer Loyalty", fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
