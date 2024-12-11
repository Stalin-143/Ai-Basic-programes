#!/bin/bash

# Bash script to set up and run the Sentiment Analysis project

echo "Starting the Sentiment Analysis setup and execution process..."

# Step 1: Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi
echo "Python3 is installed."

# Step 2: Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv sentiment_env
source sentiment_env/bin/activate
echo "Virtual environment activated."

# Step 3: Install dependencies
echo "Installing required Python libraries..."
cat > requirements.txt << EOL
nltk==3.8.1
textblob==0.17.1
transformers==4.34.0
torch==2.0.1
pandas==2.0.3
numpy==1.24.4
matplotlib==3.8.0
seaborn==0.12.2
wordcloud==1.9.2
EOL

pip install -r requirements.txt
echo "Dependencies installed."

# Step 4: Download necessary NLTK data
echo "Downloading NLTK data..."
python3 -c "import nltk; nltk.download('vader_lexicon')"

# Step 5: Write the Python script
echo "Writing the Sentiment Analysis Python script..."
cat > sentiment_analysis.py << 'EOL'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

import nltk
nltk.download('vader_lexicon')

class SentimentAnalysis:
    def __init__(self, dataset=None):
        self.dataset = dataset
        self.nlp_model = None

    def load_dataset(self, file_path=None):
        if file_path:
            self.dataset = pd.read_csv(file_path)
        else:
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

    def preprocess_data(self):
        self.dataset['Text'] = self.dataset['Text'].str.lower()
        print("\nPreprocessed Data:\n", self.dataset)

    def analyze_with_nltk(self):
        print("\nSentiment Analysis Using NLTK:")
        sia = SentimentIntensityAnalyzer()
        self.dataset['NLTK_Sentiment'] = self.dataset['Text'].apply(lambda x: sia.polarity_scores(x)['compound'])
        self.dataset['NLTK_Label'] = self.dataset['NLTK_Sentiment'].apply(
            lambda x: 'Positive' if x > 0.05 else ('Negative' if x < -0.05 else 'Neutral')
        )
        print(self.dataset[['Text', 'NLTK_Sentiment', 'NLTK_Label']])

    def analyze_with_textblob(self):
        print("\nSentiment Analysis Using TextBlob:")
        self.dataset['TextBlob_Sentiment'] = self.dataset['Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
        self.dataset['TextBlob_Label'] = self.dataset['TextBlob_Sentiment'].apply(
            lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
        )
        print(self.dataset[['Text', 'TextBlob_Sentiment', 'TextBlob_Label']])

    def analyze_with_huggingface(self):
        print("\nSentiment Analysis Using Hugging Face Transformers:")
        self.nlp_model = pipeline("sentiment-analysis")
        self.dataset['HuggingFace_Sentiment'] = self.dataset['Text'].apply(lambda x: self.nlp_model(x)[0]['label'])
        print(self.dataset[['Text', 'HuggingFace_Sentiment']])

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

sa = SentimentAnalysis()
sa.load_dataset()
sa.preprocess_data()
sa.analyze_with_nltk()
sa.analyze_with_textblob()
sa.analyze_with_huggingface()
sa.visualize_sentiments()
EOL
echo "Python script written."

# Step 6: Run the Python script
echo "Running the Sentiment Analysis script..."
python3 sentiment_analysis.py

# Step 7: Deactivate and clean up
deactivate
echo "Virtual environment deactivated."
echo "Sentiment Analysis process completed!"
