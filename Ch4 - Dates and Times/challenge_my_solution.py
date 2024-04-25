# Python code​​​​​​‌​‌‌​​​​‌​​​​​‌‌‌​​​​‌‌​​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

import calendar

def count_days(year, month, whichday):
    days = []
    y = year
    m = month
    d = whichday
    cal = calendar.monthcalendar(y,m)
    for i in cal:
        if i[:d+1] != [0]:
            days.append(i[:d+1])
    return len(days)
