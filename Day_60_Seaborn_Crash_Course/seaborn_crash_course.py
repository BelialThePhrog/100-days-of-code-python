import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load built-in Seaborn datasets
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

print("--- 1. Distribution & Categorical Plots ---")
sns.histplot(tips['total_bill'], kde=False, bins=30)
plt.title("Total Bill Distribution")
plt.show()

sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.title("Total Bill by Sex (Standard Deviation)")
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.title("Total Bill Distribution by Day and Sex")
plt.show()

print("--- 2. Matrix Plots ---")
fp = flights.pivot_table(index='month', columns='year', values='passengers')

sns.heatmap(fp, cmap='coolwarm')
plt.title("Flight Passengers Heatmap")
plt.show()

sns.clustermap(fp, cmap='coolwarm', standard_scale=1)
plt.title("Flight Passengers Clustermap")
plt.show()

print("--- 3. Grids (Iris & Tips) ---")
# PairGrid with Iris dataset
g = sns.PairGrid(iris)
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
plt.show()

# FacetGrid with Tips dataset
g_facet = sns.FacetGrid(tips, col="time", row="smoker")
g_facet.map(sns.scatterplot, "total_bill", "tip")
plt.show()

print("--- 4. Regression Plots ---")
# lmplot with customized scatter_kws
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], 
           scatter_kws={'s': 100, 'alpha': 0.7})
plt.show()

print("--- 5. Style and Context ---")
# Global style and context adjustments
sns.set_style('ticks')
sns.set_context('poster', font_scale=1.2)

sns.countplot(x='sex', data=tips)
sns.despine(left=True, bottom=True)
plt.title("Styled Countplot")
plt.show()

# Reset context to default for future plots
sns.set_context('notebook')
