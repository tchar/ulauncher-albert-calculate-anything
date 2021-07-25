from operator import sub
from itertools import zip_longest

# https://stackoverflow.com/a/30714165
def is_leap_year(year):
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def merge_dates(reference_date, dates, signs):
    if not dates:
        return 0, 0, 0, 0, 0, 0

    def extract_date_info(d): return (
        d.year, d.month, d.day, d.hour, d.minute, d.second)

    dates_stats = map(extract_date_info, dates)
    ref_date_info = extract_date_info(reference_date)
    dates_stats = map(lambda d: tuple(map(sub, d, ref_date_info)), dates_stats)

    dates_stats = zip_longest(dates_stats, signs, fillvalue=1)
    dates_stats = map(lambda d: tuple(d[1] * dd for dd in d[0]), dates_stats)

    dates_stats = zip(*dates_stats)
    dates_stats = map(sum, dates_stats)

    return tuple(dates_stats)


def parsedatetime_str(reference_date, dates, signs):
    vals = merge_dates(reference_date, dates, signs)
    info = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']

    vals = zip(vals, info)
    vals = filter(lambda v: v[0], vals)
    vals = map(lambda v: (abs(v[0]), v[1] if v[0]
               > 0 else v[1] + ' ago'), vals)
    vals = map(lambda v: '{} {}'.format(v[0], v[1]), vals)
    return ' '.join(vals)
