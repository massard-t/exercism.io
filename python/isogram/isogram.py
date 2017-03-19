import string


def is_isogram(sentence):
    sentence = sentence.lower()
    clean = list(filter(lambda x: x in string.ascii_letters, sentence))
    d = dict()
    for letter in clean:
        try:
            d[letter] += 1
            return False
        except KeyError:
            d[letter] = 1
    return True
