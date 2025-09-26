def count_chars_words(text):
    chars = len(text)
    words = len(text.split())
    return chars, words

print(count_chars_words("Natural Language Processing"))