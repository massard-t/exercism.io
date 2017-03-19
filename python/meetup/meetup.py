import calendar
import datetime


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday, qualifier):
    days = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]
    special = {
            "teenth": get_teenth,
            "last": get_last
            }
    cal = calendar.Calendar()
    month_days = cal.monthdays2calendar(year, month)
    if qualifier in special.keys():
        day = special[qualifier](month_days, days.index(weekday))
    else:
        quali_as_int = int(''.join(filter(str.isdigit, qualifier)))
        day = get_from_int(month_days, days.index(weekday), quali_as_int)
    return datetime.date(year, month, day)


def get_from_int(weeks, day, quali_as_int):
    count = 0
    for week in weeks:
        for d_date, d_week in week:
            if d_week == day and d_date != 0:
                count += 1
            if count == quali_as_int:
                print(count, d_week)
                return d_date
    raise MeetupDayException


def get_teenth(weeks, day):
    teenth = [13, 14, 15, 16, 17, 18, 19]
    for week in weeks:
        for d_date, d_week in week:
            if d_date in teenth and d_week == day:
                return d_date
    raise MeetupDayException


def get_last(weeks, day):
    l = list(reversed(weeks))
    for week in l:
        for d_date, d_week in week:
            if d_week == day and d_date != 0:
                return d_date
    raise MeetupDayException
