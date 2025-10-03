from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

def generate_wordcloud(text):
    # Your code here
    # 1- Make text lowercase then remove digits, punctuation, special characters (using regex and [^a-z\s])
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)

    # You can use a basic stopwords list
    stopwords = {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'it', 'on', 'for', 'this', 'that'}
    clean_text = ''
    # Your code here
    # 2- Remove stopwords from text and save it in clean_text
    for word in text.split():
        if word not in stopwords:
            clean_text += word + ' '

    # Create and show word cloud (this part is given, no need to change it)
    wc = WordCloud(width=800, height=400, background_color='white').generate(clean_text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

sample = """
Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems
to extract knowledge and insights from structured and unstructured data. Data science is related to data mining,
machine learning and big data. Data scientists use techniques from many fields including statistics, computer
science, and domain knowledge to analyze and interpret data. Python is one of the most popular tools in data
science because it is easy to use, flexible, and has a large number of libraries such as pandas, NumPy, scikit-learn,
and matplotlib. Python allows data scientists to clean, transform, visualize, and model data effectively.
"""
generate_wordcloud(sample)