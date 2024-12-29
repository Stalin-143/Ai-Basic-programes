import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

# Define the neural network model
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Flatten the 28x28 images into 1D vectors
    Dense(128, activation='relu'),  # Fully connected layer with 128 neurons
    Dense(64, activation='relu'),   # Fully connected layer with 64 neurons
    Dense(10, activation='softmax') # Output layer with 10 neurons for 10 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
print("Training the model...")
history = model.fit(x_train, y_train, epochs=5, validation_split=0.2, batch_size=32)

# Evaluate the model on test data
eval_results = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {eval_results[1]:.4f}")

# Save the trained model
model.save('mnist_model.h5')
print("Model saved as 'mnist_model.h5'")

# Load and use the saved model (example)
loaded_model = tf.keras.models.load_model('mnist_model.h5')
predictions = loaded_model.predict(x_test[:5])
print("Predictions for the first 5 test samples:", predictions.argmax(axis=1))
