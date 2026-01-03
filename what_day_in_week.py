def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        month_length[1] = 29

    return month_length[month - 1]


def day_of_year(year, month, day):
    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None

    total = 0
    for m in range(1, month):
        total += days_in_month(year, m)

    return total + day


def days_since_jan_1_1950(year, month, day):
    # count days from Jan 1, 1950 to target date
    total = 0

    # full years
    if year >= 1950:
        for y in range(1950, year):
            if is_year_leap(y):
                total += 366
            else:
                total += 365
    else:
        for y in range(year, 1950):
            if is_year_leap(y):
                total -= 366
            else:
                total -= 365

    # current year
    doy = day_of_year(year, month, day)
    if doy is None:
        return None

    total += doy
    return total


def what_day_in_week(year, month, day):
    days_in_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]

    total_days = days_since_jan_1_1950(year, month, day)
    if total_days is None:
        return None

    reference_weekday_index = 5  # Saturday (Jan 1, 1950)
    day_index = (reference_weekday_index + total_days) % 7

    return days_in_week[day_index]


month = int(input("Enter month: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

result = what_day_in_week(year, month, day)

print("That day is", result)
