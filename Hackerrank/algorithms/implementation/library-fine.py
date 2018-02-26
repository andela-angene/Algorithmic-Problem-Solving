day, month, year = [9, 8, 2015]
return_day, return_month, return_year = [6, 6, 2015]

if year > return_year:
    print(10000)
elif month > return_month and year == return_year:
    print(500 * (month - return_month))
elif day > return_dayi and [year, month] == [return_year, return_month]:
    print(15 * (day - return_day))
else:
    print(0)

