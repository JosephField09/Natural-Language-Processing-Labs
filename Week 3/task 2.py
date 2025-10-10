from gensim.models import Word2Vec

# Step 1: Define a small corpus (list of tokenized sentences)
corpus = [
    ["natural", "language", "processing", "is", "fun"],
    ["language", "models", "learn", "patterns"],
    ["deep", "learning", "and", "machine", "learning"],
    ["machine", "learning", "is", "part", "of", "AI"]
]

# Step 2: Train the Word2Vec model (using the method Word2Vec)
model = Word2Vec(corpus, min_count=1)

# Step 3: Find most similar words to "language" (topn=5 for top 5 similar words, using the method model.wv.most_similar)
similar_words =[]
words = model.wv.most_similar("language",topn=5)
for word in words:
    similar_words.append(word)

# Step 4: Print results
print("Most similar words to 'language':")
for word, score in similar_words:
    print(f"{word}: {score:.4f}")