import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

class HealthMonitoringSystem:
    def __init__(self, data_size=1000):
        self.data_size = data_size
        self.data = None
        self.model = None
    
    # Step 1: Generate Synthetic Data
    def generate_data(self):
        np.random.seed(42)
        
        # Simulating health metrics
        heart_rate = np.random.randint(60, 120, self.data_size)  # Normal: 60-100 bpm
        step_count = np.random.randint(0, 150, self.data_size)   # Normal: 0-150 steps
        activity = np.random.choice([0, 1, 2], size=self.data_size, p=[0.5, 0.3, 0.2])  # 0: Resting, 1: Walking, 2: Running

        # Combine into a DataFrame
        self.data = pd.DataFrame({
            "HeartRate": heart_rate,
            "StepCount": step_count,
            "Activity": activity
        })
        self.data['Timestamp'] = pd.date_range(start="2024-12-01", periods=self.data_size, freq='T')
    
    # Step 2: Data Preprocessing
    def preprocess_data(self):
        scaler = StandardScaler()
        self.data[['HeartRate', 'StepCount']] = scaler.fit_transform(self.data[['HeartRate', 'StepCount']])
    
    # Step 3: Train Activity Classification Model
    def train_model(self):
        X = self.data[['HeartRate', 'StepCount']]
        y = self.data['Activity']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Initialize Random Forest Classifier
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Cross-validation
        cv_scores = cross_val_score(self.model, X_train, y_train, cv=5, scoring='accuracy')
        print(f"Cross-Validation Accuracy Scores: {cv_scores}")
        print(f"Mean CV Accuracy: {cv_scores.mean():.4f}")

        # Train model
        self.model.fit(X_train, y_train)

        # Evaluate model
        y_pred = self.model.predict(X_test)
        print("Classification Report:\n", classification_report(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    
    # Step 4: Anomaly Detection using DBSCAN
    def detect_anomalies(self):
        dbscan = DBSCAN(eps=0.3, min_samples=10)
        anomaly_labels = dbscan.fit_predict(self.data[['HeartRate', 'StepCount']])
        self.data['Anomaly'] = anomaly_labels

        # Visualize anomalies
        anomaly_data = self.data[self.data['Anomaly'] == -1]
        print(f"Total Anomalies Detected: {len(anomaly_data)}")
        
        plt.figure(figsize=(12, 6))
        plt.scatter(self.data['Timestamp'], self.data['HeartRate'], label='Heart Rate', alpha=0.7, color='blue')
        plt.scatter(anomaly_data['Timestamp'], anomaly_data['HeartRate'], color='red', label='Anomalies')
        plt.title('Heart Rate Over Time with Anomalies')
        plt.xlabel('Timestamp')
        plt.ylabel('Normalized Heart Rate')
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
    
    # Step 5: Real-Time Data Simulation
    def simulate_real_time(self, n=10):
        print("\nReal-Time Data Simulation:\n")
        for i in range(n):
            sample = self.data.sample(1)
            print(f"Time: {sample['Timestamp'].values[0]} | "
                  f"Heart Rate: {sample['HeartRate'].values[0]:.2f} | "
                  f"Step Count: {sample['StepCount'].values[0]:.2f} | "
                  f"Activity: {self.activity_label(sample['Activity'].values[0])} | "
                  f"Anomaly: {'Yes' if sample['Anomaly'].values[0] == -1 else 'No'}")
    
    # Step 6: Health Metrics Visualization
    def plot_health_metrics(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Timestamp'], self.data['HeartRate'], label='Heart Rate', color='red', alpha=0.7)
        plt.plot(self.data['Timestamp'], self.data['StepCount'], label='Step Count', color='green', alpha=0.7)
        plt.title('Health Metrics Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Normalized Metrics')
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
    
    # Helper Method: Convert activity codes to labels
    def activity_label(self, activity_code):
        labels = {0: 'Resting', 1: 'Walking', 2: 'Running'}
        return labels.get(activity_code, 'Unknown')

# Instantiate and run the system
health_system = HealthMonitoringSystem()
health_system.generate_data()
health_system.preprocess_data()
health_system.train_model()
health_system.detect_anomalies()
health_system.simulate_real_time()
health_system.plot_health_metrics()
