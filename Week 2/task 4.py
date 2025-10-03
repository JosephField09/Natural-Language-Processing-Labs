import re

def extract_patterns(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    hashtag_pattern = r'[#]+[a-zA-Z0-9_]{1,}'
    mention_pattern = r'@[a-zA-Z]{1,}'
    url_pattern = r'http[s]?://+[a-zA-Z0-9.]{1,}'

    emails = re.findall(email_pattern, text)
    hashtags = re.findall(hashtag_pattern, text)
    mentions = re.findall(mention_pattern, text)
    urls = re.findall(url_pattern, text)

    return {
        "emails": emails,
        "hashtags": hashtags,
        "mentions": mentions,
        "urls": urls
    }

text = "Contact us at info@example.com or visit https://example.com. #news @support"
print(extract_patterns(text))