import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Load pre-trained Word2Vec model (Google News, 300-dimensional)
model = api.load("word2vec-google-news-300")  # first-time download may take time

# Step 2: Example sentences
sentence1 = "The cat sat on the mat."
sentence2 = "A dog was lying on the rug."

# Step 3: create a function to preprocess sentences: lowercase, tokenize, and return the sentence as an array
def preprocess(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(".", " ")
    sentence = sentence.split()
    result = np.array(sentence)
    return result

# Step 4: Use the function to preprocess both sentences
words1 = preprocess(sentence1)
words2 = preprocess(sentence2)

# Step 5: Create a function to get average word vectors for a sentence (we have the vector of words, but we want the vector of the full sentence)
def sentence_vector(words, model):
  vectors = []

  # Get the vector of each word from the model (using model[word]), and include it into the vector named: vectors
  for word in words:
      if word in model:
          vectors.append(model[word])

  # This step is to handle cases where no words are in the model
  if len(vectors) == 0:
    return np.zeros(model.vector_size)

  # return the "mean" of the words vectors, which is the vector of the full sentence
  return np.mean(vectors, axis=0)

# Step 6: Use "sentence_vector" for each sentence
vec1 = sentence_vector(words1, model)
vec2 = sentence_vector(words2, model)

# Compute cosine similarity between the two sentences, using "cosine_similarity" and saving the result in variable "similarity"
# [vec1] is the vector of the first sentence
# [vec2] is the vector of the second sentence
similarity = cosine_similarity([vec1], [vec2])

print("Cosine similarity between the sentences:", similarity[0][0])
