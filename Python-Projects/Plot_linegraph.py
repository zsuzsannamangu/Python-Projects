#Using the Matplotlib library, plot a simple line graph of 10 data points

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Graph')

# Display the plot
plt.show()
