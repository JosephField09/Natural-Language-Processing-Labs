import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

sample_text = "Python 3.8 is awesome!!! #coding @openAI."
print(clean_text(sample_text))