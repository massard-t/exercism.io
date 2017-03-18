import string


def is_pangram(phrase):
    l_p = list(phrase.lower())
    l_a = list(string.ascii_lowercase)
    s_p = set(l_p)
    s_a = set(l_a)
    return s_a <= s_p
