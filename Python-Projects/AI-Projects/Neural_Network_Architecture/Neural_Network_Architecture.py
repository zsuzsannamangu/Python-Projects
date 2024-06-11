import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #Suppress Tensorflow info/warning messages

import requests.packages
import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Flatten, Dense
from sklearn.model_selection import train_test_split
import ssl

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess the images by normalizing the pixel values to the range [0, 1]
# The reason for dividing by 255.0 is because in many image formats, such as RGB images, pixel values are typically represented as integers in the range [0, 255].
  # Dividing by 255.0 scales these integer values to the floating-point range [0, 1], which is suitable for many machine learning algorithms and neural networks.
X_train = X_train / 255.0
X_test = X_test / 255.0

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Define the neural network architecture creating a 'Sequential' model and adding layers ('Flatten' and two 'Dense' layers)
  # The Sequential model in Keras allows you to create a neural network by stacking layers linearly. 
  # Each layer in a Sequential model has exactly one input tensor and one output tensor. Data flows sequentially through these layers from input to output.
  # The Flatten layer is used to convert multidimensional data into a one-dimensional array
  # The Dense layer is a fully connected layer in a neural network. Each neuron in a Dense layer is connected to every neuron in the previous layer
model = Sequential([
    Flatten(input_shape=(X_train.shape[1:])),
    Dense(128, activation='relu'), # This Dense layer has 128 units, so it will produce a 128-dimensional output
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')  # Assuming 10 output classes
])

# Compile the model by specifying the optimizer, loss function, and evaluation metric
# The loss function quantifies the difference between the predicted values of the model and the actual target values in the training data, the goal is to minimize it
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {test_loss}')
print(f'Test Accuracy: {test_accuracy}')
