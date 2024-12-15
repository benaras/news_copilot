from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd

# Load your dataset
df = pd.read_csv('BBC News Train.csv')  # Replace with the actual dataset

X = df['Text']  # Text column
y = df['Category']  # Category column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize TF-IDF vectorizer
tfidf = TfidfVectorizer(max_features=500, ngram_range=(1, 3))  # Unigrams and bigrams
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Initialize the model
model = LogisticRegression(max_iter=50)
model.fit(X_train_tfidf, y_train)

# Save the model and the vectorizer
joblib.dump(model, 'news_classification_model.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
