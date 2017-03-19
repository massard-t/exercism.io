from string import ascii_lowercase, digits


def encode(sentence):
    sentence = sentence.lower()
    c_s = [c for c in sentence if c in ascii_lowercase or c in digits]
    d = gen_dic()
    res = ''
    for idx, c in enumerate(c_s):
        if not idx % 5 and idx != 0:
            res += ' '
        try:
            res += d[c]
        except KeyError:
            res += c
    return res


def decode(sentence):
    sentence = sentence.replace(' ', '')
    d = gen_dic(False)
    res = ''
    for c in sentence:
        try:
            res += d[c]
        except KeyError:
            res += c
    return res


def gen_dic(encode=True):
    keys = ascii_lowercase
    vals = reversed(ascii_lowercase)
    d = dict()
    for k, v in zip(keys, vals):
        if encode:
            d[k] = v
        else:
            d[v] = k

    return d
