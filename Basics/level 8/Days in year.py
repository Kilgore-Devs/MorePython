"""
A variation of determining leap years, assuming only integers are used and years can be negative and positive.

Write a function which will return the days in the year and the year entered in a string. For example:

year_days(2000) returns "2000 has 366 days"
There are a few assumptions we will accept the year 0, even though there is no year 0 in the Gregorian Calendar.

Also the basic rule for validating a leap year are as follows

Most years that can be divided evenly by 4 are leap years.

Exception: Century years are NOT leap years UNLESS they can be evenly divided by 400.

So the years 0, -64 and 2016 will return 366 days. Whilst 1974, -10 and 666 will return 365 days.
"""


def year_days(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return f"{x} has 366 days"
            else:
                return f"{x} has 365 days"
        else:
            return f"{x} has 366 days"
    else:
        return f"{x} has 365 days"
print(year_days(0))#, '0 has 366 days')
print(year_days(-64))#, '-6)#4 has 366 days')
print(year_days(2016))#, '2016 has 366 days')
print(year_days(1974))#, '1974 has 365 days')
print(year_days(-10))#, '-10 has 365 days')
print(year_days(666))#, '666 has 365 days')
print(year_days(1857))#, '1857 has 365 days')
print(year_days(2000))#, '2000 has 366 days')
print(year_days(-300))#, '-300 has 365 days')
print(year_days(-1))#, '-1 has 365 days')

