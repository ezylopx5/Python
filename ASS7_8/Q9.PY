import re

class Tokenizer:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        pattern = r'[\w]+|[.,!?;:]|\d+/\d+|\d+(\.\d+)?|@\w+|#\w+|https?://\S+|\w+@\w+\.\w+'
        return re.findall(pattern, self.text)

text = str(input())#Hello @john_doe! Check out https://example.com/page?query=123. Today's date is 12-02-2024. Call me at test@example.com."
tokenizer = Tokenizer(text)
# tokenizer = Tokenizer(text)
print(tokenizer.tokenize())