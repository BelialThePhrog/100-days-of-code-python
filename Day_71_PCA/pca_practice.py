"""
Principal Component Analysis (PCA) Practice
-------------------------------------------
This script applies PCA for dimensionality reduction on the 
Breast Cancer Wisconsin dataset. It scales the features and 
visualizes the principal components and their correlations.

Dataset: Breast Cancer (sklearn.datasets)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def main():
    # Load Data
    print("Loading Breast Cancer dataset...")
    cancer = load_breast_cancer()
    df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
    
    # Standardize the data
    scaler = StandardScaler()
    scaler.fit(df)
    scaled_data = scaler.transform(df)
    
    # Apply PCA
    print("Applying PCA (n_components=3)...")
    pca = PCA(n_components=3)
    pca.fit(scaled_data)
    x_pca = pca.transform(scaled_data)
    
    print(f"Original shape: {scaled_data.shape}")
    print(f"Reduced shape: {x_pca.shape}")
    
    # Visualize Principal Components (1st vs 2nd)
    plt.figure(figsize=(8, 6))
    plt.scatter(x_pca[:, 0], x_pca[:, 1], c=cancer['target'], cmap='plasma')
    plt.title("PCA: First vs Second Principal Component")
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.show()
    
    # Visualize Component Correlation Heatmap
    df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_comp, cmap='plasma')
    plt.title("PCA Component Heatmap")
    plt.show()


if __name__ == "__main__":
    main()
