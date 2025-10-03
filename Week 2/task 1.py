import string


def count_word_frequencies(sentence):
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator).lower()
    words = sentence.split()
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

print(count_word_frequencies("Data is powerful. Data drives decisions. Data, data, and more data!"))