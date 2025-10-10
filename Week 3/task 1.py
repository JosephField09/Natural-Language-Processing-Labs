from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Prepare a list of documents/sentences
documents = [
    "Natural language processing is interesting.",
    "Machine learning and natural language processing are connected.",
    "Deep learning is part of AI."
]

# Step 2: Create the TF-IDF vectorizer and fit it to the documents
vectorizer = TfidfVectorizer()
docs = vectorizer.fit_transform(documents)

# Step 3: Print the vocabulary (words and their indexes)
print(vectorizer.vocabulary_)

# Step 4: Print the TF-IDF matrix
print(docs)

# Step 5: Compute cosine similarity between document 1 and 2
cosine_similarities = cosine_similarity(docs[0], docs[1])
print(cosine_similarities)