"""
Natural Language Processing Practice
------------------------------------
This script builds a spam detection model using the SMS Spam Collection dataset.
It demonstrates custom text preprocessing (removing punctuation and stopwords) 
and the use of Scikit-Learn Pipelines for TF-IDF and Naive Bayes classification.

Dataset: SMSSpamCollection
"""

import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Ensure stopwords are downloaded
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

def text_process(mess: str) -> list:
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

def main():
    # Load Data
    print("Loading SMS Spam Collection dataset...")
    messages = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
    
    # Train-Test Split
    msg_train, msg_test, label_train, label_test = train_test_split(
        messages['message'], messages['label'], test_size=0.2, random_state=101
    )

    # Build Pipeline
    print("\nTraining NLP Pipeline (CountVectorizer -> TF-IDF -> MultinomialNB)...")
    pipeline = Pipeline([
        ('bow', CountVectorizer(analyzer=text_process)),
        ('tfidf', TfidfTransformer()),
        ('classifier', MultinomialNB())
    ])
    
    # Train and Predict
    pipeline.fit(msg_train, label_train)
    predictions = pipeline.predict(msg_test)
    
    # Evaluation
    print("\n--- Model Evaluation ---")
    print(classification_report(label_test, predictions))

if __name__ == "__main__":
    main()
