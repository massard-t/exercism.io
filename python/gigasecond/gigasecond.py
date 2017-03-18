import datetime


def add_gigasecond(base_date):
    gs = datetime.timedelta(seconds=1000000000)
    return base_date + gs
