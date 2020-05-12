import calendar

#print(calendar.monthcalendar(2020,3))
#print(calendar.month(2020,3,3))
MonthCalendar = []
for i in range(12):
    MonthCalendar.append(calendar.monthcalendar(2020,(i+1)))
#
#for i in range(len(MonthCalendar)):
#    print(MonthCalendar[i])
#    print()
#
print("leep days beween 2000 and 3000 are : " , calendar.leapdays(2000,3000))
for i in range(2000,3000):
    if calendar.isleap(i):
        print(i)