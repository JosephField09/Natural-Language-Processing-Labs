file = open("lab1_example.txt", "r")
new = open("lab1_example_updated.txt", "w")
for line in file:
    words = line.split()
    for i in range (0, len(words)):
        if words[i].lower() == "he":
            words[i] = "she"
        elif words[i].lower() == "she":
            words[i] = "he"
    new.write(f'{" ".join(words)}\n')