"""
Natural Language Processing Project
-----------------------------------
This script classifies Yelp reviews into 1-star or 5-star categories 
based on their text content. It demonstrates the use of Exploratory 
Data Analysis, Count Vectorization, TF-IDF, and Scikit-Learn Pipelines 
with a Multinomial Naive Bayes classifier.

Based on: NLP Project (Yelp Reviews) and SMS Spam Collection tutorials.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


def perform_eda(df: pd.DataFrame):
    """Generates basic exploratory data analysis visualizations."""
    print("Generating EDA visualizations...")
    sns.set_style('whitegrid')
    
    # Text length distribution by stars
    g = sns.FacetGrid(df, col="stars", height=3, col_wrap=3)
    g.map(sns.histplot, "text length")
    plt.suptitle("Text Length Distribution by Star Rating", y=1.05)
    plt.show()

    # Boxplot of text length by stars
    plt.figure(figsize=(8, 6))
    sns.boxenplot(data=df, x="stars", y="text length")
    plt.title("Boxenplot: Text Length by Stars")
    plt.show()

    # Correlation heatmap of numeric features
    plt.figure(figsize=(8, 6))
    numeric_means = df.groupby('stars').mean(numeric_only=True)
    sns.heatmap(numeric_means.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap of Mean Metrics")
    plt.show()


def evaluate_model(model_name: str, y_true: pd.Series, y_pred: pd.Series):
    """Prints formatted evaluation metrics."""
    print(f"\n--- {model_name} Evaluation ---")
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))


def main():
    # 1. Load and Prepare Data
    print("Loading Yelp dataset...")
    df = pd.read_csv('yelp.csv')
    
    # Feature Engineering: Add text length
    df['text length'] = df['text'].str.split().str.len()
    
    # Perform Exploratory Data Analysis
    perform_eda(df)

    # 2. Filter data to only 1-star and 5-star reviews
    print("\nFiltering data for 1-star and 5-star reviews...")
    yelp_class = df[(df['stars'] == 1) | (df['stars'] == 5)]
    
    X = yelp_class['text']
    y = yelp_class['stars']

    # 3. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    # 4. Baseline Model (CountVectorizer + MultinomialNB)
    print("\nTraining Baseline Model (CountVectorizer only)...")
    cv = CountVectorizer()
    X_train_cv = cv.fit_transform(X_train)
    X_test_cv = cv.transform(X_test)
    
    nb_baseline = MultinomialNB()
    nb_baseline.fit(X_train_cv, y_train)
    baseline_predictions = nb_baseline.predict(X_test_cv)
    
    evaluate_model("Baseline Model", y_test, baseline_predictions)

    # 5. Pipeline Model (CountVectorizer + TF-IDF + MultinomialNB)
    print("\nTraining Pipeline Model (includes TF-IDF)...")
    pipeline = Pipeline([
        ('bow', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('classifier', MultinomialNB())
    ])
    
    # Fit the pipeline on original text data
    pipeline.fit(X_train, y_train)
    pipeline_predictions = pipeline.predict(X_test)
    
    evaluate_model("Pipeline Model (with TF-IDF)", y_test, pipeline_predictions)


if __name__ == "__main__":
    main()
