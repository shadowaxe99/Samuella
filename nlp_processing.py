"""This module is responsible for natural language processing tasks."""

from nltk.tokenize import word_tokenize


class TextProcessor:
    def process(self, text):
        return word_tokenize(text)