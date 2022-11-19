import datetime


def is_used(cloth_date: datetime.date, c_seasons) -> bool:
    TODAY = datetime.date.today()
    if (interval := (TODAY-cloth_date).days) > 365:
        return False
    elif interval < 90:
        return True

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

    # spring, summer, autumm, winter: [0: 3]
    seasons = tuple(map(date_range_season, SEASON_RANGES))

    all_days = 0
    for i in c_seasons:
        left = seasons[i][0]
        right = seasons[i][1]
        if (left < TODAY < right):
            all_days += (TODAY-left).days
        elif left < cloth_date:
            all_days += (right-cloth_date).days
    return True if all_days <= 90 else False
