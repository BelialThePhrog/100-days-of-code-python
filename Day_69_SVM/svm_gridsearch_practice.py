"""
Support Vector Machines (SVM) & Grid Search Practice
------------------------------------------------------
This script trains a Support Vector Classifier (SVC) on the 
breast cancer dataset. It demonstrates baseline model training 
and hyperparameter tuning using GridSearchCV to improve accuracy.

Dataset: Breast Cancer (sklearn.datasets)
"""

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

def main():
    # Load Data
    cancer = load_breast_cancer()
    X = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
    y = cancer['target']

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=101
    )

    # Baseline SVC Model
    print("\n--- Baseline SVC Evaluation ---")
    model = SVC()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    # GridSearchCV for Hyperparameter Tuning
    print("\n--- GridSearchCV Evaluation ---")
    param_grid = {
        'C': [0.1, 1, 10, 100, 1000], 
        'gamma': [1, 0.1, 0.01, 0.001, 0.0001]
    }
    
    # verbose=3 displays detailed output during the grid search
    grid = GridSearchCV(SVC(), param_grid, verbose=3)
    grid.fit(X_train, y_train)
    
    print("\nBest Parameters Found:")
    print(grid.best_params_)

    # Evaluating the optimized model
    grid_predictions = grid.predict(X_test)
    
    print("\nConfusion Matrix (Optimized):")
    print(confusion_matrix(y_test, grid_predictions))
    print("\nClassification Report (Optimized):")
    print(classification_report(y_test, grid_predictions))

if __name__ == "__main__":
    main()
