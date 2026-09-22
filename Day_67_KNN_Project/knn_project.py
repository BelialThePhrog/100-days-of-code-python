"""
K Nearest Neighbors (KNN) Project
-----------------------------------
This script applies the K Nearest Neighbors algorithm to a dataset
with anonymized features. It demonstrates data standardization,
initial model evaluation, and parameter tuning using the Elbow Method.

Dataset: Classified Data
Algorithm: KNeighborsClassifier
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


def main():
    # Load Data
    df = pd.read_csv('Classified Data', index_col=0)
    print("Dataset Shape:", df.shape)

    # Standardize Features
    scaler = StandardScaler()
    scaler.fit(df.drop('TARGET CLASS', axis=1))
    scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

    df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

    # Train/Test Split
    X = df_feat
    y = df['TARGET CLASS']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    # Initial Model Training (K=1)
    print("\n--- Initial Model (K=1) ---")
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))
    print("\nClassification Report:")
    print(classification_report(y_test, pred))

    # Choosing a K Value (Elbow Method)
    print("\n--- Running Elbow Method to optimize K (1-60) ---")
    error_rate = []
    for i in range(1, 60):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        error_rate.append(np.mean(pred_i != y_test))

    # Plotting the Error Rate
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 60), error_rate, color='blue', linestyle='dashed', marker='o',
             markerfacecolor='red', markersize=8)
    plt.title('Error Rate vs. K Value')
    plt.xlabel('K')
    plt.ylabel('Error Rate')
    plt.show()

    # Final Model Training (K=40)
    print("\n--- Final Model (K=40) ---")
    knn = KNeighborsClassifier(n_neighbors=40)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))
    print("\nClassification Report:")
    print(classification_report(y_test, pred))


if __name__ == "__main__":
    main()
