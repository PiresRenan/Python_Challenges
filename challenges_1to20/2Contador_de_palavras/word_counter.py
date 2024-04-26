class WordCounter:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.strip().split()
        return len(words)
