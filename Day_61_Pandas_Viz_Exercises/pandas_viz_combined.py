import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PART 1: PRACTICE
# ==========================================
print("--- Loading Practice Data ---")
df1 = pd.read_csv('df1', index_col=0) 
df2 = pd.read_csv('df2')

print(df1.head())
print(df2.head())

# Practice: Basic scatter and area plots
df1.plot.scatter(x='A', y='B', c='C', cmap='magma')
plt.title("Practice: Scatter Plot")
plt.show()

df2.plot.area(alpha=0.4)
plt.title("Practice: Area Plot")
plt.show()


# ==========================================
# PART 2: EXERCISES
# ==========================================
print("--- Loading Exercise Data ---")
df3 = pd.read_csv('df3') 
print(df3.head())

# Recreate this scatter plot of b vs a. Note the color and size of the points.
df3.plot.scatter(x='b', y='a', cmap="magma", figsize=(12, 3)) 
plt.title("Exercise: Scatter Plot (b vs a)")
plt.show()

# Create a histogram of the 'a' column.
df3['a'].hist(bins=20) 
plt.title("Exercise: Histogram (bins=20)")
plt.show()

# Use style sheets to set the style to 'ggplot' and redo the histogram.
plt.style.use('ggplot')
df3['a'].hist(bins=30, alpha=0.7, color='orange')
plt.title("Exercise: Styled Histogram (ggplot)")
plt.show()

# Create a boxplot comparing the a and b columns.
df3.plot.box(column=('a', 'b')) 
plt.title("Exercise: Boxplot")
plt.show()

# Create a kde plot of the 'd' column.
df3['d'].plot.kde() 
plt.title("Exercise: KDE Plot")
plt.show()

# Figure out how to increase the linewidth and make the linestyle dashed.
df3['d'].plot.kde(style="--", lw=5, color="red")
plt.title("Exercise: Styled KDE Plot")
plt.show()

# Create an area plot of all the columns for just the rows up to 30.
# Display the legend outside of the plot.
df3.iloc[0:30].plot.area(alpha=0.3, stacked=True).legend(loc='center left', bbox_to_anchor=(1.0, 0.5)) 
plt.title("Exercise: Area Plot with External Legend")
plt.tight_layout()
plt.show()
