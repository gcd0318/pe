"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday. 
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine. 
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400. 
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def isLeap(y):
    return((0 == y % 400)or((0 == y % 4)and(0 != y % 100)))

def daysInMonth(y, m):
    if((4 == m)or(6 == m)or(9 == m)or(11 == m)):
        return 30
    elif(2 == m):
        if(isLeap(y)):
            return 29
        else:
            return 28
    else:
        return 31

def daysInYear(y):
    if(isLeap(y)):
        return 366
    else:
        return 365

def daysIn20C(dt):
    y = dt[0]
    m = dt[1]
    d = dt[2]
    if((1901 == y)and(1 == m)):
        return (d-1)
    elif(1901 == y):
        days = 0
        while(1 < m):
            m = m - 1
            days = days + daysInMonth(y, m)
        return(days + daysIn20C([y, 1, d]))
    else:
        days = 0
        while(1901 < y):
            y = y - 1
            days = days + daysInYear(y)
        if(isLeap(dt[0])and(2 < m)):
            return(days + daysIn20C([1901, m, d]) + 1)
        else:
            return(days + daysIn20C([1901, m, d]))

def wofd(dt):
    s = (daysInYear(1900) % 7 + 1) % 7
    y = dt[0]
    m = dt[1]
    d = dt[2]
    days = daysIn20C(dt)
    return (days+s)%7

c = 0
for y in range(1901, 2000+1):
    for m in range(1, 12+1):
        if(0 == wofd([y, m, 1])):
            c = c + 1
            print (y, m, 1)
print(c)
