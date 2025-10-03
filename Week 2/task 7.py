import matplotlib.pyplot as plt

# Usually the dataset is saved in a file (txt or CSV file), and we 'll have to open/read the data and save it in a list variable but in this is a simple example
# Example dataset: list of (sentence, label)
data = [
    ("I love this product!", "positive"),
    ("This is the worst experience ever.", "negative"),
    ("It was okay, nothing special.", "neutral"),
    ("Amazing service and quality!", "positive"),
    ("Not worth the price.", "negative"),
    ("Quite good overall.", "positive")
]

# Extract labels from the dataset, and save it in a list called labels
labels = []
# Code here
# Create a loop that goes through the dataset (data) and extract the value of label, then add that value to the list "labels"
for i in range(len(data)):
    labels.append(data[i][1])
# How many unique label is used in the dataset?
unique_labels = list(set(labels))

# Count occurrences of each label
counts = []
# Code here
# Create a loop that goes through the list "unique_labels"
# Then count each of the unique labels in the list labels (hint: you can use the method count(): list_name.count(the_value_to_count) )
# Add that count value to the list "counts"
for i in range(len(unique_labels)):
    counts.append(labels.count(unique_labels[i]))

# Plot - Draw a bar chart
plt.bar(unique_labels, counts)
plt.title("Count of Each Label")
plt.ylabel("Number of Sentences")
plt.xlabel("Labels")
plt.show()
