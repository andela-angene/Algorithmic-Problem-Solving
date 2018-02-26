def check_leap(year, isGregorian):
    if isGregorian:
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return year % 4 == 0


def programmer_day(year):
    result = ['23', '09', str(year)]
    if year == 1918:
        return '.'.join(result)

    leap = check_leap(year, False) if year < 1918 else check_leap(year, True)
    result[0] = '12' if leap else '13'

    return '.'.join(result)


print(programmer_day(1918))
print(programmer_day(2017))
print(programmer_day(2016))
print(programmer_day(1040))
