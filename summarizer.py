import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter
import heapq

nltk.download('punkt')

class TextSummarizer:
    def __init__(self, text):
        self.text = text

    def summarize(self, num_sentences=3):
        sentences = sent_tokenize(self.text)

        # Word frequency
        word_frequencies = Counter(word.lower() for sentence in sentences for word in sentence.split())

        # Scoring sentences
        sentence_scores = {sentence: sum(word_frequencies[word.lower()] for word in sentence.split()) for sentence in sentences}

        # Selecting top sentences
        summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        
        return ' '.join(summary_sentences)
