#Implement the gradient descent algorithm for a simple linear regression
#In this code, we first generate random data points X and y. We then initialize the weights w and bias b, 
#set the number of iterations and learning rate, and perform gradient descent to update the weights and bias. 
#Finally, we plot the data points and the regression line, and print the final weights and bias.

import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 3 + 4 * X + np.random.randn(100, 1)

# Number of iterations and learning rate
iterations = 1000
learning_rate = 0.01

# Initialize weights and bias
w = np.random.randn(1, 1)
b = np.random.randn(1)

# Perform gradient descent
for i in range(iterations):
    # Compute predictions
    y_pred = np.dot(X, w) + b
    
    # Compute gradients
    dw = -2 * np.dot(X.T, (y - y_pred)) / len(X)
    db = -2 * np.sum(y - y_pred) / len(X)
    
    # Update weights and bias
    w -= learning_rate * dw
    b -= learning_rate * db

# Plot the data points
plt.scatter(X, y, label='Data points')

# Plot the regression line
plt.plot(X, y_pred, color='red', label='Regression line')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()

# Print the final weights and bias
print('Final weights:', w)
print('Final bias:', b)
