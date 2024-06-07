import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from flask import Flask, request, render_template
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Load the dataset
df = pd.read_csv("/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Sentiment_Analysis/Sentiment_Analysis_Dataset.csv")

# Ensure balanced classes
print(df['sentiment'].value_counts())

# Select the columns for sentiment analysis
text_column = 'text'
sentiment_column = 'sentiment'

# Check class balance
positive_count = len(df[df[sentiment_column] == 'Positive'])
negative_count = len(df[df[sentiment_column] == 'Negative'])

print(f"Positive: {positive_count}, Negative: {negative_count}")

# Preprocess the text data
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    text = text.split()  # Split into words
    text = [ps.stem(word) for word in text if not word in stop_words]  # Stemming and remove stop words
    text = ' '.join(text)
    return text

X = df[text_column].apply(preprocess_text)
y = df[sentiment_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Vectorize the text data
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Try different models
models = {
    'LogisticRegression': LogisticRegression(max_iter=1000),
    'RandomForest': RandomForestClassifier(n_estimators=100)
}

# Perform cross-validation and print results
for model_name, model in models.items():
    cv_scores = cross_val_score(model, X_train_vectorized, y_train, cv=5, scoring='accuracy')
    print(f"{model_name} CV Accuracy: {cv_scores.mean()}")

# Train the best model on the full training set
best_model = LogisticRegression(max_iter=1000)
best_model.fit(X_train_vectorized, y_train)

# Make predictions on the testing set
y_pred = best_model.predict(X_test_vectorized)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Positive')
recall = recall_score(y_test, y_pred, pos_label='Positive')
f1 = f1_score(y_test, y_pred, pos_label='Positive')

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sentence = request.form['sentence']
        sentence_cleaned = preprocess_text(sentence)
        sentence_vectorized = vectorizer.transform([sentence_cleaned])
        prediction = best_model.predict(sentence_vectorized)
        return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
