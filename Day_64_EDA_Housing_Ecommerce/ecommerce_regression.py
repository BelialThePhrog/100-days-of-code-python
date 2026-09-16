"""
Ecommerce Customer Spending Prediction — Linear Regression
------------------------------------------------------------
An e-commerce company sells clothing online and in-store. Customers
get styling advice in person, then order via a mobile app or website.
This script models which engagement metric best predicts how much a
customer spends per year, to help the company decide where to invest:
the app or the website.

Dataset: Ecommerce Customers
Target:  Yearly Amount Spent
Features: Avg. Session Length, Time on App,
          Time on Website, Length of Membership
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

sns.set_style("whitegrid")


def load_data(path: str = "Ecommerce Customers") -> pd.DataFrame:
    """Load the customer dataset and print a quick summary."""
    df = pd.read_csv(path)
    print("Shape:", df.shape)
    print(df.head())
    print(df.info())
    print(df.describe())
    return df


def explore_data(df: pd.DataFrame) -> None:
    """Visualize relationships between engagement metrics and spending."""
    sns.jointplot(data=df, x="Time on Website", y="Yearly Amount Spent")
    plt.show()

    sns.jointplot(data=df, x="Time on App", y="Yearly Amount Spent")
    plt.show()

    sns.jointplot(
        data=df, x="Time on App", y="Length of Membership", kind="hex"
    )
    plt.show()

    sns.pairplot(df)
    plt.show()

    # Length of Membership shows the clearest linear relationship
    # with Yearly Amount Spent
    sns.lmplot(data=df, x="Length of Membership", y="Yearly Amount Spent")
    plt.show()


def train_model(df: pd.DataFrame):
    """Split the data and fit a linear regression model."""
    feature_cols = [
        "Avg. Session Length",
        "Time on App",
        "Time on Website",
        "Length of Membership",
    ]
    X = df[feature_cols]
    y = df["Yearly Amount Spent"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=101
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
    plt.xlabel("Actual Yearly Amount Spent")
    plt.ylabel("Predicted Yearly Amount Spent")
    plt.title("Actual vs. Predicted Spending")
    plt.show()

    mae = metrics.mean_absolute_error(y_test, predictions)
    mse = metrics.mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)

    print(f"\nMAE:  {mae:,.2f}")
    print(f"MSE:  {mse:,.2f}")
    print(f"RMSE: {rmse:,.2f}")

    sns.histplot((y_test - predictions), kde=True)
    plt.title("Residuals Distribution")
    plt.show()


def main():
    df = load_data()
    explore_data(df)
    model, X_test, y_test = train_model(df)
    evaluate_model(model, X_test, y_test)

    print(
        "\nConclusion: Length of Membership is the strongest predictor of "
        "yearly spending. Time on App contributes more than Time on "
        "Website, suggesting the company gets a better return from "
        "investing further in the mobile app — though building out the "
        "website to catch up could be an equally valid strategy."
    )


if __name__ == "__main__":
    main()
