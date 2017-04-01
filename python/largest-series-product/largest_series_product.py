from operator import mul


def largest_product(serie, sub_serie_length):
    lsum = []
    if sub_serie_length == 0:
        return 1
    if len(serie) < sub_serie_length or sub_serie_length < 0:
        raise ValueError
    for idx, _ in enumerate(serie):
        res = 1
        tmp = list(map(int, serie[idx:idx+sub_serie_length]))
        if len(tmp) < sub_serie_length:
            continue
        for ele in tmp:
            res *= ele
        lsum += [res]

    return max(lsum) if max(lsum) else 0
