# month and number of days of month
month_day_rule = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


# check if a year is a leap year
def is_leap_year(_year):

    if _year % 4 != 0:
        return False
    elif (_year % 4 == 0 and _year % 100 != 0) or _year % 400 == 0:
        print(str(_year) + " is a leap year")
        return True
    else:
        return False


# return the nearest leap year in a range
def top_leap_year_in_range(year1, year2):
    for year in range(year2, year1, -1):
        if is_leap_year(year):
            return year
            break
    else:
        print("no leap year in range")
        return 0


# return farthest leap year in a range
def bottom_leap_year_in_range(year1, year2):
    for year in range(year1, year2):
        if is_leap_year(year):
            return year
            break
    else:
        print("no leap year in range")


# count number of leap years in a range
def number_of_leap_years_in_range(year1, year2):
    top_leap_year = top_leap_year_in_range(year1, year2)
    bottom_leap_year = bottom_leap_year_in_range(year1, year2)
    return (top_leap_year - bottom_leap_year)/4 + 1


# count days from 1st day of the year to current day
def days_from_1st_jan_to_current_day(current_day):
    days_of_current_year = 0
    days_of_full_months = 0

    if current_day["month"] != 1:
        for month in range(1, current_day["month"]):
            days_of_full_months += month_day_rule[month]

            # if this is a leap year and current month is Feb -> then need add 1 day (become 29 days)
            if is_leap_year(current_day["year"]) and month == 2:
                days_of_full_months += 1

    # add days of current month
    days_of_current_year += days_of_full_months + current_day["day"]
    return days_of_current_year


# count days from current day to last day of the year
def days_from_current_to_last(current_day):
    days_of_current_year = days_from_1st_jan_to_current_day(current_day)
    if is_leap_year(current_day["year"]):
        return 366 - days_of_current_year + 1   # count 1 day that I was born
        # return 366 - days_of_current_year   # don't count 1 day that I was born
    else:
        return 365 - days_of_current_year + 1
        # return 365 - days_of_current_year


def age_in_days(birthday, today):
    days_in_current_year = days_from_1st_jan_to_current_day(today)
    days_left_in_birth_year = days_from_current_to_last(birthday)
    leap_years_in_range = number_of_leap_years_in_range(birthday["year"]+1, today["year"]-1)
    number_of_full_years_in_range = today["year"] - birthday["year"] - 1
    total_days_of_age = \
        number_of_full_years_in_range * 365 + leap_years_in_range * 1 + days_in_current_year + days_left_in_birth_year
    return total_days_of_age


if __name__ == '__main__':

    my_birthday = {
        "day": 12,
        "month": 5,
        "year": 1996
    }
    current_date = {
        "day": 29,
        "month": 11,
        "year": 2018
    }

    print("my_birthday: " + str(my_birthday))
    print("current day: " + str(current_date))
    print("ages in days: " + str(age_in_days(my_birthday, current_date)))
