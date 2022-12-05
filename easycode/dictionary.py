from collections import defaultdict

def countLetters(word):
    counter = defaultdict(lambda: 0)
    for letter in word:
        counter[letter] += 1

    return counter