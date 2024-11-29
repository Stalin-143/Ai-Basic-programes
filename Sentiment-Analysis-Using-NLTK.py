import nltk
from nltk.corpus import movie_reviews
from random import shuffle
import string
import re

# Download necessary data
nltk.download("movie_reviews")
nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

def preprocess(text):
    # Remove punctuation and lowercase the text
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    return text

def get_features(text):
    words = nltk.word_tokenize(text)
    words = [w for w in words if w not in stopwords.words("english")]
    return {word: True for word in words}

def load_dataset():
    # Load movie reviews dataset from NLTK
    labeled_reviews = [
        (list(movie_reviews.words(fileid)), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)
    ]
    shuffle(labeled_reviews)
    return labeled_reviews

def train_model():
    # Prepare the dataset
    dataset = load_dataset()
    featuresets = [(get_features(" ".join(words)), label) for words, label in dataset]
    split = int(len(featuresets) * 0.8)
    train_set, test_set = featuresets[:split], featuresets[split:]

    # Train Naive Bayes Classifier
    classifier = NaiveBayesClassifier.train(train_set)
    print(f"Model Accuracy: {accuracy(classifier, test_set):.2f}")
    return classifier

def sentiment_analysis():
    print("Training model...")
    classifier = train_model()
    print("\nSentiment Analysis Program")
    print("Type 'exit' to stop the program.")
    
    while True:
        text = input("\nEnter a sentence: ")
        if text.lower() == "exit":
            print("Goodbye!")
            break

        # Preprocess and classify the input text
        processed_text = preprocess(text)
        features = get_features(processed_text)
        sentiment = classifier.classify(features)
        print(f"Sentiment: {sentiment.capitalize()}")

# Run the program
if __name__ == "__main__":
    sentiment_analysis()
