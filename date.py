import datetime
import sys


def _try_create_date(x):
    try:
        year, month, day = x
        if year < 2000:
            year += 2000
        return datetime.date(year, month, day)
    except ValueError:
        return None


def parse(date_str):
    a, b, c = (int(x) for x in date_str.split('/', 2))

    force_year = ''
    if a >= 2000:
        force_year = 'a'
    elif b >= 2000:
        force_year = 'b'
    elif c >= 2000:
        force_year = 'c'

    permutations = [
        (a, b, c) if force_year in ('a', '') else None,
        (a, c, b) if force_year in ('a', '') else None,
        (b, a, c) if force_year in ('b', '') else None,
        (b, c, a) if force_year in ('b', '') else None,
        (c, a, b) if force_year in ('c', '') else None,
        (c, b, a) if force_year in ('c', '') else None,
    ]

    dates = [_try_create_date(x) for x in permutations if x is not None]
    dates = [x for x in dates if x is not None]

    if len(dates) == 0:
        return "is illegal"
    else:
        return min(dates).strftime("%Y-%m-%d")


def main():
    with open(sys.argv[1], "rt") as f:
        print(parse(f.read().strip()))


if __name__ == '__main__':
    main()

__all__ = ["parse"]
