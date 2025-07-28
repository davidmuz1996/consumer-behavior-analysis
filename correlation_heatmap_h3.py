import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define mock data for Spearman correlations between perceived offensiveness (5 types)
# and 3 behavioral reaction variables

offensive_types = [
    "Sexual Content",
    "Violent Imagery",
    "Stereotypes (Gender/Race)",
    "Religious Offense",
    "Cynical/Dark Humor"
]

reaction_vars = [
    "Stopped Buying",
    "Social Media Role",
    "Public Reaction Intent"
]

# Create a mock correlation matrix (Spearman r-values)
np.random.seed(42)
r_values = np.random.uniform(low=-0.1, high=0.5, size=(5, 3))
p_values = np.random.uniform(low=0.001, high=0.2, size=(5, 3))

# Round the values for presentation
r_values = np.round(r_values, 2)
p_values = np.round(p_values, 3)

# Create a combined DataFrame for output
rows = []
for i, offensive in enumerate(offensive_types):
    for j, reaction in enumerate(reaction_vars):
        rows.append({
            "Offensive Message Type": offensive,
            "Reaction Variable": reaction,
            "Spearman r": r_values[i][j],
            "p-value": p_values[i][j]
        })

df_corr = pd.DataFrame(rows)
print(df_corr)

data = {
    'Stopped Buying': [-0.05, 0.24, 0.12, -0.08, 0.11],
    'Social Media Role': [0.39, 0.35, 0.31, 0.04, 0.22],
    'Public Reaction Intent': [0.43, 0.17, 0.29, -0.03, 0.19]
}
index = ['Violent Content', 'Cynical Humor', 'Stereotypes', 'Religious Offense', 'Sexual Content']

df = pd.DataFrame(data, index=index)

plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='RdBu_r', center=0)
plt.title('Spearman Correlations between Perceived Offensive Messages and Consumer Reactions')
plt.xlabel('Consumer Response Variable')
plt.ylabel('Type of Offensive Message')
plt.tight_layout()
plt.show()