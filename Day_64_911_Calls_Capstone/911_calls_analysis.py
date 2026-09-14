import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# DATA LOADING & SETUP
# ==========================================
print("--- Loading 911 Data ---")
df = pd.read_csv("911.csv") 

# ==========================================
# FEATURE ENGINEERING
# ==========================================
# Extract specific Reason from the title column (e.g., 'EMS: BACK PAINS/INJURY' -> 'EMS')
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0]) 

# Convert timeStamp strings to Datetime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp']) 

# Extract time-based features
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour) 
df['Month'] = df['timeStamp'].apply(lambda time: time.month) 
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek) 

# Map Day of Week integers to strings
dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'} 
df['Day of Week'] = df['Day of Week'].map(dmap)

# Extract Date for time-series aggregation
df['Date'] = df['timeStamp'].apply(lambda t: t.date()) 

# ==========================================
# EXPLORATORY DATA ANALYSIS & VISUALIZATION
# ==========================================

# 1. Countplot of 911 calls by Reason
sns.countplot(x='Reason', data=df) #[cite: 17]
plt.title('Total 911 Calls by Reason')
plt.show()

# 2. Countplot of Day of Week with Reason hue
sns.countplot(x='Day of Week', data=df, hue='Reason') 
plt.title('911 Calls by Day of Week')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# 3. Countplot of Month with Reason hue
sns.countplot(x='Month', data=df, hue='Reason') 
plt.title('911 Calls by Month')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# 4. Linear Regression Fit on calls per month
byMonth = df.groupby('Month').count().reset_index() 
sns.lmplot(x='Month', y='Reason', data=byMonth, scatter_kws={'s': 100}) 
plt.title('Linear Fit of Calls per Month')
plt.show()

# 5. Time Series Plot of Total Calls
df.groupby('Date').count()['twp'].plot() 
plt.title('Total Calls by Date')
plt.tight_layout()
plt.show()

# 6. Time Series Plots separated by Reason
for reason in ['Traffic', 'Fire', 'EMS']:
    df[df['Reason'] == reason].groupby('Date').count()['twp'].plot()
    plt.title(f'{reason} Calls by Date')
    plt.tight_layout()
    plt.show()
