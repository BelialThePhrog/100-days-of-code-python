"""
K-Means Clustering Practice
---------------------------
This script demonstrates the K-Means clustering algorithm using 
artificial data generated with make_blobs. It visualizes the 
clusters and evaluates the performance using the Adjusted Rand Score.

Dataset: Artificial (make_blobs)
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

def main():
    # Generate Artificial Data
    print("Generating artificial data with 4 clusters...")
    data = make_blobs(n_samples=400, n_features=2, centers=4, cluster_std=1.8, random_state=101)
    
    # Visualize Original Data
    sns.set_style('whitegrid')
    plt.figure(figsize=(8, 6))
    plt.scatter(data[0][:, 0], data[0][:, 1], c=data[1], cmap='rainbow')
    plt.title("Original Artificial Data")
    plt.show()

    # K-Means Cluster Creation (n_clusters=4)
    print("\n--- Training K-Means Model (n_clusters=4) ---")
    # Setting random_state for reproducibility, though not explicitly in original fit
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(data[0])

    print("\nCluster Centers:")
    print(kmeans.cluster_centers_)

    # Visualize: K-Means vs Original
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10, 6))
    ax1.set_title('K Means')
    ax1.scatter(data[0][:, 0], data[0][:, 1], c=kmeans.labels_, cmap='rainbow')
    
    ax2.set_title("Original")
    ax2.scatter(data[0][:, 0], data[0][:, 1], c=data[1], cmap='rainbow')
    plt.show()

    # Evaluation
    # ARI scores from -1 to 1 (where 1.0 is a perfect match)
    score = adjusted_rand_score(data[1], kmeans.labels_)
    print(f"\nClustering accuracy (Adjusted Rand Score): {score}")

if __name__ == "__main__":
    main()
