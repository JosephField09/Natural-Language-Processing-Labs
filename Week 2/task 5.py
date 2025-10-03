import re

def text_stats(text):
    # Split paragraphs by double newline (and ignore empty paragraphs)
    paragraphs = text.split("\n\n")
    # Then count the number of paragraphs and save in a variable num_paragraphs
    num_paragraphs = len(paragraphs)

    # Count sentences by splitting on '.', '!', '?' (and ignore empty strings)
    sentences = re.split(r'[.?!]+', text)
    # Then count the number of sentences and save in a variable num_sentences
    num_sentences = len(sentences)

    return num_sentences, num_paragraphs

sample_text = """This is the first sentence! This is a test.

This is a new paragraph? Yes, it is!

And here is another one."""

sentences, paragraphs = text_stats(sample_text)
print(f"Sentences: {sentences}, Paragraphs: {paragraphs}")