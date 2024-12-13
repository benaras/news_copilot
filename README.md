# News Co-Pilot: Personalized News Recommendation System

## Project Overview
News Co-Pilot is an AI-powered platform designed to personalize news content for users. By leveraging machine learning and natural language processing (NLP) techniques, the system classifies news articles and tailors recommendations based on user preferences. The project uses public datasets and cutting-edge AI methodologies to address the challenge of information overload in today’s digital age.

---

## Objectives and Goals
1. **Classify News Articles**: Build robust models to categorize articles into predefined topics like Politics, Sports, Technology, etc.
2. **Personalize Recommendations**: Develop algorithms to recommend articles tailored to users’ reading history and preferences.
3. **Enhance User Experience**: Provide intuitive visualizations and user-friendly interfaces for accessing categorized and personalized news.
4. **Promote Accessibility**: Ensure the platform is inclusive and accessible to diverse audiences.

---

## Methodology

### Data Collection
- **Dataset Used**: BBC News Articles dataset from Kaggle.
- The dataset contains articles with associated topics for supervised learning.
- https://www.kaggle.com/c/learn-ai-bbc/data?select=BBC+News+Test.csv 

### Data Preprocessing
- Text cleaning (removal of stopwords, punctuation, and special characters).
- Tokenization and stemming/lemmatization.
- Transformation into numerical features using TF-IDF and word embeddings.

### Modeling
1. **Text Classification**:
   - Models used: Logistic Regression, Naive Bayes, Random Forest, and BERT-based transformers.
   - Metrics: Accuracy, Precision, Recall, and F1-score.
2. **Personalized Recommendation**:
   - Collaborative filtering and content-based filtering.
   - Evaluated using precision@k and recall@k.

### Implementation Tools
- **Libraries**: Scikit-learn, TensorFlow, Keras, Pandas, Numpy, and Matplotlib.
- **Platforms**: Google Colab for training and GitHub for version control.
- **Programming Languages**: Python for coding and SQL for querying data.

---

## Results and Key Findings
- **Model Accuracy**:
  - Logistic Regression: 85%
  - Random Forest: 88%
  - BERT: 92%
- **Personalization Metrics**:
  - Precision@5: 78%
  - Recall@5: 74%
- The transformer-based model (BERT) outperformed traditional methods for text classification.
- Feedback-based refinement improved recommendation relevance over iterations.

---

## Visualizations
1. **Confusion Matrix**: Displays the classification performance for each topic.
2. **Word Clouds**: Highlights prominent keywords for each topic category.
3. **Recommendation Dashboard**: Shows top articles recommended to users.
4. **Model Performance Graphs**: Accuracy and loss plots during training.

---

## Potential Next Steps
1. **Expand Dataset**:
   - Incorporate real-time data scraping from RSS feeds and news websites.
2. **Enhance Recommendations**:
   - Implement reinforcement learning for dynamic personalization.
3. **Improve Accessibility**:
   - Add multilingual support for global reach.
4. **Deployment**:
   - Host the model as a web application for public access.

---

## Individual Contributions

### Shachi Benara
- Coordinated team tasks and set deadlines using GitHub and Google Colab.
- Created the slideshow
### Yujia (Stella) Zhai
- 

### Henok Misgina (Henok) Fisseha
- 
