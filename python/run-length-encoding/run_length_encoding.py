import string


def encode(text):
    if not text:
        return ""
    counter = 0
    old = ''
    res = ""
    changed = False
    for letter in text:
        if old == '':
            old = letter
            counter += 1
            continue
        if letter == old:
            counter += 1
            changed = False
        else:
            disp = str(counter) if counter > 1 else ''
            res += disp + old
            old = letter
            counter = 1
            changed = True
    if not changed:
        disp = str(counter) if counter > 1 else ''
        res += disp + old
    else:
        disp = str(counter) if counter > 1 else ''
        res += disp + letter
    return res


def decode(text):
    res = ''
    nbrs = string.digits
    tmp = ''
    if not text:
        return ""
    for char in text:
        if char in nbrs:
            tmp += char
            continue
        else:
            if tmp != '':
                times = int(tmp)
                res += char*times
                tmp = ''
            else:
                res += char
    return res
