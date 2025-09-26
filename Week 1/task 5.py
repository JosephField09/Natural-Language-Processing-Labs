file = open("lab1_example.txt", "r")
for line in file:
    words = line.split()
    if len(words) > 3:
        print(line)