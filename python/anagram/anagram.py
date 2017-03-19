def same_letters(initials, arg1):
    letters = sorted(initials.lower())
    arg = sorted(arg1.lower())
    if arg == letters and initials != arg:
        return True
    return False


def detect_anagrams(initials, words):
    if initials == words[0]:
        return []
    return list(filter(lambda x: same_letters(initials, x), words))
