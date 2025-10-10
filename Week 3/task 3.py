from transformers import BertTokenizer, BertModel
import torch

# Step 1: Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Step 2: Sentence to encode
sentence = "Using Bert to generate word embeddings."

# Step 3: Tokenize (using tokenizer), use the variable name "inputs"
inputs = tokenizer(sentence, return_tensors='pt')

# Step 4: Forward pass through BERT: Feed input data into the BERT model and get the output vectors (embeddings)
with torch.no_grad():
    outputs = model(**inputs)

# Step 5: Get the first token token embedding, use variable name "cls_embedding" (using outputs.last_hidden_state)
cls_embedding = outputs.last_hidden_state

# Step 6: Convert token IDs back to words to print them in Step 7, use variable name "tokens" (this step is nor essential but only done to print the token as words in Step 7)
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0]) 


# Step 7: Print embeddings for each token
for token, embedding in zip(tokens, cls_embedding[0]):
  print(f"{token:12} → {embedding[:5]}...")  # Show only first 5 values for brevity
print('-----------------------------------------------------------------------------')
# Step 8: Print the embedding vector
print("CLS token embedding (sentence vector):")
print(cls_embedding)