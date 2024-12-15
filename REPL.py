import joblib

# Load the saved model and vectorizer
model = joblib.load('news_classification_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

# Start REPL
print("News Classification REPL")
print("Type 'exit' or 'quit' to stop the program.")

while True:
    # Get user input
    text = input("Enter news text: ")
    
    # Check for exit condition
    if text.lower() in ['exit', 'quit']:
        print("Exiting...")
        break
    
    # Preprocess and predict
    try:
        text_vectorized = tfidf.transform([text])  # Vectorize the input
        prediction = model.predict(text_vectorized)  # Predict the category
        print(f"\n\nPredicted Category: {prediction[0]} \n\n")
    except Exception as e:
        print(f"Error: {e}")
