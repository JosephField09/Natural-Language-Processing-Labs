# For tf-idf:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example sentences
sentence1 = "The cat sat on the mat."
sentence2 = "A dog was lying on the rug."

sentences = [sentence1, sentence2]

# Step 1: Create TF-IDF vectors using TfidfVectorizer and save the created word vectors in variable "tfidf_matrix"
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

# Step 2: Compute cosine similarity between the two sentences, using "cosine_similarity" and saving the result in variable "similarity"
# tfidf_matrix[0:1] is the vector of the first sentence
# tfidf_matrix[1:2] is the vector of the second sentence
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

# Print the vectors values and the similarity value
print("TF-IDF Vectors:\n", tfidf_matrix.toarray())
print("\nCosine Similarity between the sentences:", similarity[0][0])