"""
USA Housing Price Prediction — Linear Regression
--------------------------------------------------
Predicts house prices from area-level demographic and housing
statistics using scikit-learn's LinearRegression.

Dataset: USA_Housing.csv
Target:  Price
Features: Avg. Area Income, Avg. Area House Age,
          Avg. Area Number of Rooms, Avg. Area Number of Bedrooms,
          Area Population
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

sns.set_style("whitegrid")


def load_data(path: str = "USA_Housing.csv") -> pd.DataFrame:
    """Load the housing dataset and print a quick summary."""
    df = pd.read_csv(path)
    print("Shape:", df.shape)
    print(df.info())
    print(df.describe())
    return df


def explore_data(df: pd.DataFrame) -> None:
    """Visualize feature distributions and correlations."""
    sns.pairplot(df)
    plt.suptitle("Pairwise Feature Relationships", y=1.02)
    plt.show()

    sns.histplot(df["Price"], kde=True)
    plt.title("Distribution of House Prices")
    plt.show()

    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.show()


def train_model(df: pd.DataFrame):
    """Split the data and fit a linear regression model."""
    feature_cols = [
        "Avg. Area Income",
        "Avg. Area House Age",
        "Avg. Area Number of Rooms",
        "Avg. Area Number of Bedrooms",
        "Area Population",
    ]
    X = df[feature_cols]
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=101
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    coefficients = pd.DataFrame(
        model.coef_, index=feature_cols, columns=["Coefficient"]
    )
    print("\nModel Coefficients:")
    print(coefficients)

    return model, X_test, y_test


def evaluate_model(model, X_test, y_test) -> None:
    """Generate predictions and report standard regression metrics."""
    predictions = model.predict(X_test)

    plt.scatter(y_test, predictions, alpha=0.6)
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs. Predicted House Prices")
    plt.show()

    sns.histplot((y_test - predictions), kde=True)
    plt.title("Residuals Distribution")
    plt.show()

    mae = metrics.mean_absolute_error(y_test, predictions)
    mse = metrics.mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)

    print(f"\nMAE:  {mae:,.2f}")
    print(f"MSE:  {mse:,.2f}")
    print(f"RMSE: {rmse:,.2f}")


def main():
    df = load_data()
    explore_data(df)
    model, X_test, y_test = train_model(df)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()
