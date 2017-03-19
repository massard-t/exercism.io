def slices(numbers, length):
    if len(numbers) < length or length < 1:
        raise ValueError("Invalid parameter: length")
    res = []
    for index, ele in enumerate(numbers):
        try:
            res.append(list(map(int, numbers[index:index+length])))
        except IndexError:
            break
    return list(filter(lambda x: len(x) == length, res))
