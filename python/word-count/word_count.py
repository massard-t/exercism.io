# -*- coding: utf-8  -*-
import re


def word_count(phrase):
    phrase = re.sub("[\W]|_", " ", phrase, re.UNICODE)
    p_l = phrase.lower().split()
    d = dict()
    for ele in p_l:
        try:
            d[ele] += 1
        except KeyError:
            d[ele] = 1
    return d
