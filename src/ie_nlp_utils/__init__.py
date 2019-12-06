"""
IE NLP utils (sample Python project).
"""

__version__ = "0.1.dev0"


def sum_numbers(a, b):
    return a + b

def tokenize(sentence, lower=False):
    if lower:
        sentence = sentence.lower()

    return sentence.split()
