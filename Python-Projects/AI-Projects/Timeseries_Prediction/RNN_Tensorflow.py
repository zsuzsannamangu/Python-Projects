#Implement an RNN for a time series prediction using TensorFlow

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Generate synthetic time series data (a sine wave with added noise)
np.random.seed(0)
n_points = 1000
time = np.arange(0, n_points)
sin_wave = np.sin(time * 0.1) + np.random.randn(n_points) * 0.1

# Split the data into input (X) and target sequences (y)
seq_length = 10
X = []
y = []
for i in range(len(sin_wave) - seq_length):
    X.append(sin_wave[i:i + seq_length])
    y.append(sin_wave[i + seq_length])

X = np.array(X)
y = np.array(y)

# Reshape the data for RNN input
X = X.reshape(-1, seq_length, 1)
y = y.reshape(-1, 1)

# Define the RNN model
model = tf.keras.Sequential([
    tf.keras.layers.SimpleRNN(64, input_shape=(seq_length, 1), activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X, y, epochs=50, batch_size=32, validation_split=0.1)

# Plot training loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()

# Generate predictions using the trained model
predicted = model.predict(X)

# Plot the actual vs predicted values
plt.plot(time[:-seq_length], sin_wave[:-seq_length], label='Actual')
plt.plot(time[:-seq_length], predicted, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Actual vs Predicted')
plt.legend()
plt.show()