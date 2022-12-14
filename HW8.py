from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"Bob": (2001, 12, 22)},
    {"Alisa": (1999, 12, 16)},
    {"Mike": (1995, 12, 17)},
]

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def happy_birthday(users, day=7):
    current_date = datetime.now().date()
    end = current_date + timedelta(days=day)

    dct = defaultdict(list)

    for user in users:
        for name, birthday in user.items():
            str_b = [str(b) for b in birthday]
            str_b[0] = str(current_date.year)
            str_b = " ".join(str_b)
            birthday = datetime.strptime(str_b, '%Y %m %d')
            birthday = datetime.strptime(str_b, "%Y %m %d")
            birthday = birthday.date()

            if current_date <= birthday < end:
                w_day = birthday.weekday()
                if w_day not in (5, 6):
                    dct[birthday].append(name)
                elif w_day == 5:
                    dct[birthday + timedelta(days=2)].append(name)
                elif w_day == 6:
                    dct[birthday + timedelta(days=1)].append(name)
            else:
                continue
    return dct


if __name__ == "__main__":
    dt: datetime
    for dt, pers in happy_birthday(users).items():
        print(f"{dt.strftime('%A')} ({dt}) : {pers}")
