def time_conversion(s):
    if s[:2] == '12' and s[-2:] == 'AM':
        return '00' + s[2:-2]
    elif s[-2:] == 'PM' and s[:2] != '12':
        hour = int(s[:2]) + 12
        return str(hour) + s[2:-2]
    else:
        return s[:-2]


print(time_conversion('12:00:00AM'))
print(time_conversion('12:00:01AM'))
print(time_conversion('01:00:00AM'))
print(time_conversion('07:05:45PM'))
print(time_conversion('11:05:45PM'))
print(time_conversion('11:20:01AM'))
print(time_conversion('12:20:00PM'))
print(time_conversion('12:00:00PM'))
