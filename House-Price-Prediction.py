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
data = pd.read_csv('house_prices.csv')  # Replace with your dataset path

# Display dataset information
print(data.info())
print(data.describe())

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Encode categorical variables
data = pd.get_dummies(data, drop_first=True)

# Split features and target
X = data.drop('Price', axis=1)  # Replace 'Price' with the target column name
y = data['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

# Evaluate Random Forest Model
rf_mse = mean_squared_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)
print(f"Random Forest MSE: {rf_mse}")
print(f"Random Forest R²: {rf_r2}")

# Neural Network Model
nn_model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)
])

nn_model.compile(optimizer='adam', loss='mse')

# Train Neural Network
history = nn_model.fit(X_train, y_train, validation_split=0.2, epochs=100, batch_size=32, verbose=1)

# Predict using Neural Network
nn_predictions = nn_model.predict(X_test).flatten()

# Evaluate Neural Network Model
nn_mse = mean_squared_error(y_test, nn_predictions)
nn_r2 = r2_score(y_test, nn_predictions)
print(f"Neural Network MSE: {nn_mse}")
print(f"Neural Network R²: {nn_r2}")

# Visualize Loss Curves
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Neural Network Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Visualize Predictions
plt.scatter(y_test, rf_predictions, alpha=0.6, label='Random Forest Predictions')
plt.scatter(y_test, nn_predictions, alpha=0.6, label='Neural Network Predictions')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2, label='Ideal Predictions')
plt.title('Predicted vs Actual House Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.legend()
plt.show()
