"""
Titanic Survival Prediction — Logistic Regression Practice
------------------------------------------------------------
This script cleans the Titanic dataset, handles missing data
via custom imputation, converts categorical features into dummy variables,
and trains a Logistic Regression model to predict passenger survival.

Dataset: titanic_train.csv
Algorithm: LogisticRegression
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

sns.set_style("whitegrid")


def impute_age(cols):
    """Impute missing ages based on passenger class average."""
    Age = cols.iloc[0]
    Pclass = cols.iloc[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


def main():
    # Load Data
    train = pd.read_csv('titanic_train.csv')
    print("Initial Data Info:")
    train.info()

    # Exploratory Data Analysis (EDA)
    sns.heatmap(train.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing Data Map")
    plt.show()

    sns.countplot(x='Survived', data=train, hue='Pclass')
    plt.title("Survival by Passenger Class")
    plt.show()

    sns.boxplot(x='Pclass', y='Age', data=train)
    plt.title("Age Distribution by Passenger Class")
    plt.show()

    # Data Cleaning
    train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)
    train.drop('Cabin', axis=1, inplace=True)
    train.dropna(inplace=True)

    # Feature Engineering (Dummy Variables)
    sex = pd.get_dummies(train['Sex'], drop_first=True)
    embark = pd.get_dummies(train['Embarked'], drop_first=True)
    
    train = pd.concat([train, sex, embark], axis=1)
    train.drop(['Sex', 'Embarked', 'Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)

    # Train/Test Split
    X = train.drop('Survived', axis=1)
    y = train['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

    # Model Training
    logmodel = LogisticRegression(max_iter=1000)
    logmodel.fit(X_train, y_train)

    # Predictions & Evaluation
    predictions = logmodel.predict(X_test)
    print("\nClassification Report (Titanic):")
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    main()
