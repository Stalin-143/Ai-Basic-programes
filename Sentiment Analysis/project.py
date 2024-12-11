import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

# Install necessary libraries if not already installed
# pip install nltk textblob transformers wordcloud matplotlib seaborn pandas

import nltk
nltk.download('vader_lexicon')

class SentimentAnalysis:
    def __init__(self, dataset=None):
        self.dataset = dataset
        self.nlp_model = None

    # Step 1: Load Dataset
    def load_dataset(self, file_path=None):
        if file_path:
            self.dataset = pd.read_csv(file_path)
        else:
            # Example dataset
            self.dataset = pd.DataFrame({
                'Text': [
                    "I love this product! It's amazing.",
                    "This is the worst thing I've ever bought.",
                    "It's okay, not the best but not the worst.",
                    "Absolutely fantastic experience!",
                    "Terrible, I hate it.",
                    "The quality is great, but the price is too high.",
                    "Decent product for the price.",
                    "I wouldn't recommend it to anyone.",
                    "It's perfect, just what I needed!",
                    "Not bad, but it could be better."
                ]
            })
        print("\nDataset Loaded:\n", self.dataset)

    # Step 2: Data Preprocessing
    def preprocess_data(self):
        self.dataset['Text'] = self.dataset['Text'].str.lower()  # Convert to lowercase
        print("\nPreprocessed Data:\n", self.dataset)

    # Step 3: Sentiment Analysis with NLTK
    def analyze_with_nltk(self):
        print("\nSentiment Analysis Using NLTK:")
        sia = SentimentIntensityAnalyzer()
        self.dataset['NLTK_Sentiment'] = self.dataset['Text'].apply(lambda x: sia.polarity_scores(x)['compound'])
        self.dataset['NLTK_Label'] = self.dataset['NLTK_Sentiment'].apply(
            lambda x: 'Positive' if x > 0.05 else ('Negative' if x < -0.05 else 'Neutral')
        )
        print(self.dataset[['Text', 'NLTK_Sentiment', 'NLTK_Label']])

    # Step 4: Sentiment Analysis with TextBlob
    def analyze_with_textblob(self):
        print("\nSentiment Analysis Using TextBlob:")
        self.dataset['TextBlob_Sentiment'] = self.dataset['Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
        self.dataset['TextBlob_Label'] = self.dataset['TextBlob_Sentiment'].apply(
            lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
        )
        print(self.dataset[['Text', 'TextBlob_Sentiment', 'TextBlob_Label']])

    # Step 5: Sentiment Analysis with Hugging Face Transformers
    def analyze_with_huggingface(self):
        print("\nSentiment Analysis Using Hugging Face Transformers:")
        self.nlp_model = pipeline("sentiment-analysis")
        self.dataset['HuggingFace_Sentiment'] = self.dataset['Text'].apply(lambda x: self.nlp_model(x)[0]['label'])
        print(self.dataset[['Text', 'HuggingFace_Sentiment']])

    # Step 6: Visualization
    def visualize_sentiments(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(x='NLTK_Label', data=self.dataset, palette='coolwarm')
        plt.title("Sentiment Distribution (NLTK)")
        plt.show()

        plt.figure(figsize=(12, 6))
        sns.countplot(x='TextBlob_Label', data=self.dataset, palette='viridis')
        plt.title("Sentiment Distribution (TextBlob)")
        plt.show()

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(self.dataset['Text']))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud of Sentences")
        plt.show()

# Run Sentiment Analysis
sa = SentimentAnalysis()
sa.load_dataset()  # Load the sample dataset
sa.preprocess_data()
sa.analyze_with_nltk()
sa.analyze_with_textblob()
sa.analyze_with_huggingface()
sa.visualize_sentiments()
