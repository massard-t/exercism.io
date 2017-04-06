from string import ascii_lowercase as alphabet


def rotate(string, idx):
    res = ''
    for l in string:
        lower = l.islower()
        if l.lower() in alphabet:
            i = (alphabet.index(l.lower())+idx)%26
            letter = alphabet[i]
            if lower:
                res += letter
            else:
                res += letter.upper()
            continue
        res += l
    return res
