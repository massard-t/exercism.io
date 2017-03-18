def is_leap_year(year):
    div_4 = year % 4 == 0
    div_100 = year % 100 == 0
    div_400 = year % 400 == 0
    if not div_4:
        return False
    if div_400:
        return True
    if div_100:
        return False
    return True
