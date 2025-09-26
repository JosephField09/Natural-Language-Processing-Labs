def split_and_print(sentence):
    words = sentence.split()
    words = sorted(words, key=len)
    for word in words:
        print(f"{word} -> {len(word)}")

split_and_print("This is a sample sentence.")