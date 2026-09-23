"""
Lending Club Random Forest Project
------------------------------------
Explores historical lending data to classify and predict whether 
a borrower paid back their loan in full. Includes extensive EDA 
and categorical feature engineering.

Dataset: loan_data.csv
Algorithms: DecisionTreeClassifier, RandomForestClassifier
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def explore_data(df: pd.DataFrame) -> None:
    """Perform Exploratory Data Analysis and data visualization."""
    # FICO distributions by credit policy
    plt.figure(figsize=(10, 6))
    df[df['credit.policy'] == 1]['fico'].hist(alpha=0.5, color='blue', bins=30, label='Credit.Policy=1')
    df[df['credit.policy'] == 0]['fico'].hist(alpha=0.5, color='red', bins=30, label='Credit.Policy=0')
    plt.legend()
    plt.xlabel('FICO')
    plt.title('FICO Score by Credit Policy')
    plt.show()

    # FICO distributions by not.fully.paid
    plt.figure(figsize=(10, 6))
    df[df['not.fully.paid'] == 1]['fico'].hist(alpha=0.5, color='blue', bins=30, label='not.fully.paid=1')
    df[df['not.fully.paid'] == 0]['fico'].hist(alpha=0.5, color='red', bins=30, label='not.fully.paid=0')
    plt.legend()
    plt.xlabel('FICO')
    plt.title('FICO Score by Payment Status')
    plt.show()

    # Purpose vs Payment Status
    plt.figure(figsize=(11, 5))
    sns.countplot(data=df, hue='not.fully.paid', x='purpose', palette='Set1')
    plt.title('Loan Purpose by Payment Status')
    plt.tight_layout()
    plt.show()

    # FICO vs Interest Rate Trend
    sns.jointplot(data=df, x='fico', y='int.rate', color='purple')
    plt.show()

    # Lmplots for trend comparison
    sns.lmplot(y='int.rate', x='fico', data=df, hue='credit.policy', col='not.fully.paid', palette='Set1')
    plt.show()

def main():
    # Load Data
    loans = pd.read_csv('loan_data.csv')
    print("Dataset Info:")
    loans.info()

    # Execute EDA
    explore_data(loans)

    # Feature Engineering (Dealing with categorical feature 'purpose')
    cat_feats = ['purpose']
    final_data = pd.get_dummies(loans, columns=cat_feats, drop_first=True)

    # Train/Test Split
    X = final_data.drop('not.fully.paid', axis=1)
    y = final_data['not.fully.paid']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    # Single Decision Tree
    print("\n--- Decision Tree Evaluation ---")
    dtree = DecisionTreeClassifier()
    dtree.fit(X_train, y_train)
    dt_pred = dtree.predict(X_test)
    print(confusion_matrix(y_test, dt_pred))
    print(classification_report(y_test, dt_pred))

    # Random Forest Model
    print("\n--- Random Forest Evaluation ---")
    rfc = RandomForestClassifier(n_estimators=300)
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    print(confusion_matrix(y_test, rfc_pred))
    print(classification_report(y_test, rfc_pred))

if __name__ == "__main__":
    main()
