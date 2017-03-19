def sum_of_multiples(n, multiples):
    res = set()
    for i in range(n):
        for m in multiples:
            if m and not i % m:
                res.add(i)
    return sum(res)
