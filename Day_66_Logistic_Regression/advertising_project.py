"""
Advertising Ad Click Prediction — Logistic Regression Project
---------------------------------------------------------------
Analyzes an advertising dataset to predict whether an internet
user will click on an ad based on features like time spent on site,
age, area income, and internet usage.

Dataset: advertising.csv
Algorithm: LogisticRegression
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

sns.set_style("whitegrid")


def explore_data(data: pd.DataFrame) -> None:
    """Visualize data distributions and relationships."""
    sns.histplot(x='Age', data=data, bins=30)
    plt.title("Age Distribution")
    plt.show()

    sns.jointplot(x='Age', y="Area Income", data=data)
    plt.show()

    sns.jointplot(x='Age', y="Daily Time Spent on Site", data=data, kind="kde")
    plt.show()

    sns.jointplot(x='Daily Time Spent on Site', y="Daily Internet Usage", data=data)
    plt.show()

    sns.pairplot(data, hue='Clicked on Ad')
    plt.show()


def main():
    # Load Data
    data = pd.read_csv('advertising.csv')
    print("Dataset Shape:", data.shape)
    print("\nData Info:")
    data.info()
    print("\nData Describe:")
    print(data.describe())

    # Exploratory Data Analysis
    explore_data(data)

    # Feature Selection
    feature_cols = ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']
    X = data[feature_cols]
    y = data['Clicked on Ad']

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Model Training
    logmodel = LogisticRegression(max_iter=1000)
    logmodel.fit(X_train, y_train)

    # Predictions & Evaluation
    predictions = logmodel.predict(X_test)
    print("\nClassification Report (Advertising):")
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    main()
