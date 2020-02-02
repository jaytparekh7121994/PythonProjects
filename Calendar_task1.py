import calendar
import openpyxl

# Setting Sunday as First Week of the Month
ls = []
count = 0
calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.monthrange(2020, 1)

week_list = calendar.monthcalendar(2020, 1)
print(cal)
for i in week_list:
    print(i)
    count += 1
    print("Week", count)
    for j in i:
        if (j == 0):
            print("ignore")
        else:
            print("Weekdays = ", j)

iterable_week = calendar.Calendar(firstweekday=6).iterweekdays()
for i in iterable_week:
    if (i == 5 or i == 6):
        print("weekend")
    else:
        print("weekday", i)
print(week_list)
# print(week_list[0])

copyweeklist = week_list.copy()
# jan_holiday = [1,2,3]
#
output = None
len (week_list) - week_list.count(0)

# for weekno in range(0, len(week_list)):
#     for dayno in range(0, len(week_list[weekno])):
#         # if week_list[weekno][dayno] :
        #     print( )
