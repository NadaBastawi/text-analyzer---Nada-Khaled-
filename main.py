#!/usr/bin/env python3
import re
from collections import Counter

TOKEN_REGEX = re.compile(r"""
    [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}   # emails
  | \d+\.\d+(?:[eE][+-]?\d+)?                       # decimal numbers with optional exponent
  | \d+(?:[eE][+-]?\d+)?\b                           # integers with optional exponent
  | [A-Za-z0-9]+(?:-[A-Za-z0-9]+)+                      # hyphenated words
  | [A-Za-z]+(?:'[A-Za-z]+)+                            # contractions
  | [A-Za-z0-9_]+                                       # regular words/numbers
""", re.VERBOSE)

SENTENCE_END_REGEX = re.compile(r'(?<!\d)([.!?]+)(?=\s|$)')

def load_text(path='sample_text.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def tokenize(text):
    return [m.group(0) for m in TOKEN_REGEX.finditer(text)]

def count_sentences(text):
    matches = SENTENCE_END_REGEX.findall(text)
    return len(matches)

def analyze(text):
    tokens = tokenize(text)
    total_words = len(tokens)
    total_sentences = count_sentences(text)
    freqs = Counter(t.lower() for t in tokens)
    top10 = freqs.most_common(10)
    return total_words, total_sentences, top10

def print_report(total_words, total_sentences, top10):
    print(f'Total words: {total_words}')
    print(f'Total sentences: {total_sentences}')
    print('Top 10 words:')
    for word, count in top10:
        print(f'  {word} — {count}')

def main():
    text = load_text()
    total_words, total_sentences, top10 = analyze(text)
    print_report(total_words, total_sentences, top10)

if __name__ == '__main__':
    main()
