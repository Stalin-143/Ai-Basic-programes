# PowerShell script to set up and run the Sentiment Analysis project on Windows

Write-Host "Starting the Sentiment Analysis setup and execution process..." -ForegroundColor Green

# Step 1: Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python from https://www.python.org/downloads/ and try again." -ForegroundColor Red
    exit 1
}
Write-Host "Python is installed." -ForegroundColor Green

# Step 2: Create a virtual environment
Write-Host "Creating a virtual environment..." -ForegroundColor Cyan
python -m venv sentiment_env
if (-not (Test-Path "sentiment_env")) {
    Write-Host "Failed to create virtual environment. Exiting..." -ForegroundColor Red
    exit 1
}
Write-Host "Virtual environment created." -ForegroundColor Green

# Step 3: Activate the virtual environment
Write-Host "Activating the virtual environment..." -ForegroundColor Cyan
& .\sentiment_env\Scripts\Activate.ps1
if (-not $?) {
    Write-Host "Failed to activate virtual environment. Exiting..." -ForegroundColor Red
    exit 1
}
Write-Host "Virtual environment activated." -ForegroundColor Green

# Step 4: Create requirements.txt and install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Cyan
@"
nltk==3.8.1
textblob==0.17.1
transformers==4.34.0
torch==2.0.1
pandas==2.0.3
numpy==1.24.4
matplotlib==3.8.0
seaborn==0.12.2
wordcloud==1.9.2
"@ > requirements.txt
pip install -r requirements.txt

# Step 5: Download NLTK data
Write-Host "Downloading NLTK data..." -ForegroundColor Cyan
python -c "import nltk; nltk.download('vader_lexicon')"
Write-Host "NLTK data downloaded." -ForegroundColor Green

# Step 6: Write the Python script
Write-Host "Writing the Sentiment Analysis Python script..." -ForegroundColor Cyan
@'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

import nltk
nltk.download("vader_lexicon")

class SentimentAnalysis:
    def __init__(self, dataset=None):
        self.dataset = dataset
        self.nlp_model = None

    def load_dataset(self, file_path=None):
        if file_path:
            self.dataset = pd.read_csv(file_path)
        else:
            self.dataset = pd.DataFrame({
                "Text": [
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
        self.dataset["Text"] = self.dataset["Text"].str.lower()
        print("\nPreprocessed Data:\n", self.dataset)

    def analyze_with_nltk(self):
        print("\nSentiment Analysis Using NLTK:")
        sia = SentimentIntensityAnalyzer()
        self.dataset["NLTK_Sentiment"] = self.dataset["Text"].apply(lambda x: sia.polarity_scores(x)["compound"])
        self.dataset["NLTK_Label"] = self.dataset["NLTK_Sentiment"].apply(
            lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral")
        )
        print(self.dataset[["Text", "NLTK_Sentiment", "NLTK_Label"]])

    def analyze_with_textblob(self):
        print("\nSentiment Analysis Using TextBlob:")
        self.dataset["TextBlob_Sentiment"] = self.dataset["Text"].apply(lambda x: TextBlob(x).sentiment.polarity)
        self.dataset["TextBlob_Label"] = self.dataset["TextBlob_Sentiment"].apply(
            lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
        )
        print(self.dataset[["Text", "TextBlob_Sentiment", "TextBlob_Label"]])

    def analyze_with_huggingface(self):
        print("\nSentiment Analysis Using Hugging Face Transformers:")
        self.nlp_model = pipeline("sentiment-analysis")
        self.dataset["HuggingFace_Sentiment"] = self.dataset["Text"].apply(lambda x: self.nlp_model(x)[0]["label"])
        print(self.dataset[["Text", "HuggingFace_Sentiment"]])

    def visualize_sentiments(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(x="NLTK_Label", data=self.dataset, palette="coolwarm")
        plt.title("Sentiment Distribution (NLTK)")
        plt.show()

        plt.figure(figsize=(12, 6))
        sns.countplot(x="TextBlob_Label", data=self.dataset, palette="viridis")
        plt.title("Sentiment Distribution (TextBlob)")
        plt.show()

        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(self.dataset["Text"]))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud of Sentences")
        plt.show()

sa = SentimentAnalysis()
sa.load_dataset()
sa.preprocess_data()
sa.analyze_with_nltk()
sa.analyze_with_textblob()
sa.analyze_with_huggingface()
sa.visualize_sentiments()
'@ > sentiment_analysis.py
Write-Host "Python script written." -ForegroundColor Green

# Step 7: Run the Python script
Write-Host "Running the Sentiment Analysis script..." -ForegroundColor Cyan
python sentiment_analysis.py

# Step 8: Deactivate virtual environment and clean up
Write-Host "Deactivating virtual environment..." -ForegroundColor Cyan
.\sentiment_env\Scripts\Deactivate.ps1
Write-Host "Sentiment Analysis process completed!" -ForegroundColor Green
