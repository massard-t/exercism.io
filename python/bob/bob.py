def hey(sentence):
    sentence = sentence.rstrip('\t\n ')
    if sentence.strip() == '':
        return 'Fine. Be that way!'
    elif sentence.isupper():
        return 'Whoa, chill out!'
    elif sentence.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
