def count_words_in_file(filename):
    text = open(filename, "r").read()
    words = text.split()
    return len(words)

def count_lines_in_file(filename):
    text = open(filename, "r").read()
    lines = text.split("\n")
    return len(lines)

print(count_words_in_file("lab1_example.txt"))
print(count_lines_in_file("lab1_example.txt"))