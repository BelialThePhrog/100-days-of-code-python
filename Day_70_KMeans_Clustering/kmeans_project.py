"""
K Means Clustering Project
--------------------------
This script applies the K-Means unsupervised learning algorithm 
to cluster universities into two groups (Private vs. Public) 
based on their features, and evaluates the performance using 
the actual labels.

Dataset: College_Data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report


def converter(cluster: str) -> int:
    """Converts Private 'Yes'/'No' labels into binary format."""
    if cluster == 'Yes':
        return 1
    else:
        return 0


def main():
    # Load Data
    df = pd.read_csv('College_Data', index_col=0)
    print("Dataset Shape:", df.shape)
    
    # Exploratory Data Analysis (EDA)
    sns.set_style('whitegrid')
    
    # Scatterplot: Grad.Rate vs Room.Board
    sns.lmplot(x='Room.Board', y='Grad.Rate', data=df, hue='Private',
               palette='coolwarm', height=6, aspect=1, fit_reg=False)
    plt.title("Graduation Rate vs Room & Board")
    plt.show()

    # Scatterplot: F.Undergrad vs Outstate
    sns.lmplot(x='Outstate', y='F.Undergrad', data=df, hue='Private',
               palette='coolwarm', height=6, aspect=1, fit_reg=False)
    plt.title("Full-time Undergraduates vs Out-of-state Tuition")
    plt.show()

    # Stacked Histogram: Outstate Tuition
    g = sns.FacetGrid(df, hue="Private", palette='coolwarm', height=6, aspect=2)
    g.map(plt.hist, 'Outstate', bins=20, alpha=0.7)
    plt.title("Out of State Tuition Distribution")
    plt.show()

    # Stacked Histogram: Graduation Rate
    g = sns.FacetGrid(df, hue="Private", palette='coolwarm', height=6, aspect=2)
    g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.7)
    plt.title("Graduation Rate Distribution")
    plt.show()

    # Data Cleaning: Fix graduation rate over 100%
    print("\nFixing Cazenovia College Graduation Rate anomaly...")
    df.loc['Cazenovia College', 'Grad.Rate'] = 100

    # K Means Cluster Creation
    print("\n--- Training K-Means Model (n_clusters=2) ---")
    kmeans = KMeans(n_clusters=2, random_state=101)
    
    # Fit the model to all data except the target 'Private' label
    kmeans.fit(df.drop('Private', axis=1))

    # Evaluation
    # Create a new 'Cluster' column mapping Private status to 1 and Public to 0
    df['Cluster'] = df['Private'].apply(converter)

    print("\n--- K-Means Evaluation ---")
    print("Confusion Matrix:")
    print(confusion_matrix(df['Cluster'], kmeans.labels_))
    
    print("\nClassification Report:")
    print(classification_report(df['Cluster'], kmeans.labels_))


if __name__ == "__main__":
    main()
