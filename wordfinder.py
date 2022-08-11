"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, path):
        """reads # of words in dictionary"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print (f"{len(self.words)} words red")

    def parse (self, dict_file):
        """parse dict_file and return a list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """returns a random word"""
        return random.choice(self.words)

class SpecialWordFinder:

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]