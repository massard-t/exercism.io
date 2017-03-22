import datetime

UNIT = 1000000000


def add_gigasecond(base_date):
    return base_date + datetime.timedelta(seconds=UNIT)
