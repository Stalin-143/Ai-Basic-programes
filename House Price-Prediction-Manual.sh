#!/bin/bash

# Bash Script to Guide Through House Price Prediction Project

# Step 1: Setup Python Environment
echo "Setting up Python environment..."
python3 -m venv house_price_env
source house_price_env/bin/activate
pip install --upgrade pip

# Step 2: Install Required Libraries
echo "Installing required libraries..."
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow

# Step 3: Create Project Structure
echo "Creating project structure..."
mkdir -p house_price_project/{data,notebooks,models}
echo "# House Price Prediction Project" > house_price_project/README.md

# Step 4: Prepare Dataset
echo "Place your dataset in the 'house_price_project/data' directory"

# Step 5: Generate Python Script
echo "Generating Python script for house price prediction..."
cat <<EOL > house_price_project/house_price_prediction.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load dataset
data = pd.read_csv('data/house_prices.csv')  # Replace with your dataset path

# Data preprocessing steps
# Code for data cleaning and preprocessing...

# Model training and evaluation steps
# Code for Random Forest and Neural Network models...
EOL

# Step 6: Run the Script
echo "Navigate to the project directory and run the script:"
echo "cd house_price_project"
echo "python house_price_prediction.py"

# Step 7: Clean Up
echo "To deactivate the environment, run: deactivate"
echo "To remove the environment and files, delete the 'house_price_env' directory."
