import re


def abbreviate(sentence):
    r = '[A-Z]+[a-z]*|[a-z]+'
    return ''.join(word[0].title() for word in re.findall(r, sentence))
