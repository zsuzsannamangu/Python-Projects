#Supervised Machine Learning and Model Evaluation Assignment

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset from CSV
file_path = '/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Supervised_MachineLearning/exampledataset1.csv'
data = pd.read_csv(file_path)

# Split the dataset into features (X) and target (y)
X = data.drop('Target', axis=1)
y = data['Target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model using the training data
# Logistic regression is a statistical model (a classification algorithm) used for binary classification tasks, 
   # where the goal is to predict a binary outcome (e.g., yes/no, 1/0, true/false). 
model = LogisticRegression() # Specifying the model to use
model.fit(X_train, y_train) # We do the training with the fit() function

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model's performance by calculating the accuracy score on the testing data
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy score
print(f'Accuracy Score: {accuracy}')

