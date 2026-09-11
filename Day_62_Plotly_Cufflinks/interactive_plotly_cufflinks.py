import numpy as np
import pandas as pd
import cufflinks as cf
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# ==========================================
# ENVIRONMENT SETUP
# ==========================================
# Enable offline mode for interactive plots
cf.go_offline()

# Set Pandas plotting backend to Plotly
pd.options.plotting.backend = "plotly"

# ==========================================
# DATA PREPARATION
# ==========================================
print("--- Generating and Loading Data ---")
# Generating a 100x4 DataFrame with random values
df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

# Creating a categorical DataFrame
df1 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})

print("Data Sample (df):")
print(df.head())

print("\nData Sample (df1):")
print(df1.head())

# ==========================================
# INTERACTIVE VISUALIZATION
# ==========================================
print("\n--- Generating Interactive Plot ---")
# Generate an interactive line plot for all columns in 'df'
# Applying a custom color sequence ('gold')
fig = df.plot(color_discrete_sequence=['gold'])

# Display the interactive plot (opens in browser if run as a script)
fig.show()
