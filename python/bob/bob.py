import re


def hey(sentence):
    sentence = sentence.rstrip('\t\n ')
    if len(sentence) == 0:
        return "Fine. Be that way!"
    elif sentence == sentence.upper() and not sentence[-1] == '?':
        return 'Whoa, chill out!'
    elif sentence[-1] == '?':
        return "Sure."
    elif not re.search('[a-zA-Z]', sentence):
        return 'Whatever.'
    else:
        return "Whatever."
