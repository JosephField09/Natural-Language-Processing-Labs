pos_dict = {
    "run": "VB",
    "runs": "VBZ",
    "running": "VBG",
    "ran": "VBD",
    "dog": "NN",
    "dogs": "NNS",
    "cat": "NN",
    "cats": "NNS",
    "happy": "JJ",
    "happier": "JJR",
    "happiest": "JJS",
    "quickly": "RB",
    "slowly": "RB",
    "blue": "JJ",
    "sky": "NN",
    "eat": "VB",
    "eats": "VBZ",
    "ate": "VBD",
    "eaten": "VBN",
    "think": "VB",
    "thinks": "VBZ",
    "thought": "VBD",
    "thoughts": "NNS",
    "beautiful": "JJ",
    "beauty": "NN",
    "and": "CC",
    "or": "CC",
    "but": "CC",
    "because": "IN",
    "although": "IN"
}

def lookup_pos(word, pos_dict):
    if word in pos_dict:
        return pos_dict[word]
    else:
        return "Not Found"

print(lookup_pos("beautiful", pos_dict))
print(lookup_pos("unknown", pos_dict)) 