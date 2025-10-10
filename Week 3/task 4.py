from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load pretrained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Step 2: Sentences to compare
sentence1 = "The cat sat on the mat."
sentence2 = "A dog was lying on the rug."

# Step 3: create a function to get a vector for a sentence
def get_sentence_vector(sentence):
    # Step A: Turn sentence into tokens
    inputs = tokenizer(sentence, return_tensors='pt')

    # Step B: Get output from BERT
    outputs = model(**inputs)

    # Step 3: Extract the first token vector
    cls_vector = outputs.last_hidden_state[0, 0]
    return cls_vector

# Step 4: Get the vectors for each sentence (using get_sentence_vector)
vec1 = get_sentence_vector(sentence1)
vec2 = get_sentence_vector(sentence2)

# Step 5 : Convert vectors to numpy arrays and reshape for similarity calculation
vec1_np = vec1.detach().numpy().reshape(1, -1)
vec2_np = vec2.detach().numpy().reshape(1, -1)

'''
Notes:
cosine_similarity expects input arrays of shape (n_samples, n_features) : that is, a 2D array where each row is one sample/vector.
The BERT [CLS] vector is a 1D array (just one vector), so we need to reshape it to (1, vector_length)
using .reshape(1, -1) to make it a 2D array with 1 sample.

For example (5,) -> (1,5)
'''

# Step 6: Calculate cosine similarity using cosine_similarity (value between 0 and 1), save the result in variable "similarity_score"
similarity_score = cosine_similarity(vec1_np, vec2_np)

print("Similarity score:", similarity_score)