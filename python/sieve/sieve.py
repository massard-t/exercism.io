import re


def sieve(n):
    return list(filter(
        lambda x: not re.match(r'^1?$|^(11+?)\1+$', '1' * x), range(n+1)))
