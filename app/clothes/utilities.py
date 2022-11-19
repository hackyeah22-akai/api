import datetime

# spring, summer, autumm, winter: [0: 3]
TODAY = datetime.date.today()


def date_range_season(params):
    R = datetime.date(*params[0])
    L = datetime.date(*params[1])
    if R < TODAY < L:
        return (R, L)
    if R > TODAY and L > TODAY:
        return (
            datetime.date(R.year-1, R.month, R.day),
            datetime.date(L.year-1, L.month, L.day)
        )
    return (R, L)


ty = TODAY.year
SEASON_RANGES = (
    ((ty, 3, 21), (ty, 6, 21)),
    ((ty, 6, 22), (ty, 9, 22)),
    ((ty, 9, 23), (ty, 12, 21)),
    ((ty, 12, 22), (ty+1, 3, 20))
)

SEASONS = tuple(map(date_range_season, SEASON_RANGES))


def is_used(cloth_date: datetime.date, c_seasons) -> bool:
    all_days = 0
    for i in c_seasons:
        left = SEASONS[i][0]
        right = SEASONS[i][1]
        if (left < cloth_date < right):
            all_days += (right-cloth_date).days
        else:
            all_days += (right-left).days
    return True if all_days <= 90 else False
