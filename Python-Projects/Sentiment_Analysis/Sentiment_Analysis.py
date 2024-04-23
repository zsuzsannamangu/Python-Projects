#Natural Language Processing Sentiment Analysis Assignment

#Import the necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#Load the dataset
df = pd.read_csv("/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Sentiment_Analysis/exampledataset2.csv")

#Select the columns for sentiment analysis
text_column = 'text' #The text column contains the text data for sentiment analysis, the features
sentiment_column = 'sentiment' #The sentiment column contains the sentiment labels, the target

#Split the dataset into features (X) and target (y)
X = df[text_column]
y = df[sentiment_column]

#Split the data into training and testing sets
#Specify the desired test size as 0.2 for 20% of the data, and a random seed for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Vectorize the text data
#Vectorizing text data is the process of converting textual data into numerical vectors that machine learning models can understand and process
#In the context of sentiment analysis, vectorizing text data allows machine learning models like SVM to learn patterns and associations between words and sentiments
vectorizer = CountVectorizer() #Create an instance of the 'CountVectorizer' class
X_train_vectorized = vectorizer.fit_transform(X_train) #Fit the vectorizer on the training text data ('X_train') to convert it into a document-term matrix
X_test_vectorized = vectorizer.transform(X_test) #Transform the testing text data ('X_test')

#Initialize the SVM classifier (Support Vector Machines is a machine learning model)
svm_classifier = SVC() #Create an instance of the 'SVC' class

#Train the model
svm_classifier.fit(X_train_vectorized, y_train) #Pass the vectorized training data ('X_train') and the corresponding sentiment labels ('y_train') to the 'fit()' method

#Make predictions on the testing set
y_pred = svm_classifier.predict(X_test_vectorized) #Use the trained model to make predictions on the vectorized testing data ('X_test') and create the predicted labels

#Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred) #Use the 'accuracy_score()' function to compare the predicted labels (y_pred) with the true labels (y_test), 
                                          #assign the calculated accuracy to the variable 'accuracy'

#Print the accuracy of the model
print(f"Accuracy of the SVM model: {accuracy}")


