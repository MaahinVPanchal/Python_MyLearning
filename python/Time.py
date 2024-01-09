# Get the current time:-
# To get the current time in Python, at first, import the time module:

import time;
mytime =  time.localtime(time.time())
print("Current time = ",mytime)

# Get the number of seconds passed since epoch
sec = time.time()
print("No of seconds passed since epoch = ",sec)

# Python calendar module
# The calendar module in Python is used to perform calendar operations such as displaying calendar of a year, calendar of a month, etc.

import calendar

# For calendar, use the calendar() method with parameters: 
# calendar(y, width, line, col)

# y = year
# width = width of characters
# Line: no. of lines
# col = column separations

print("2023 calender = ")
print(calendar.calendar(2023,2,1,9))

# Get the calendar of a month
year = 2020
month = 6
print("Calendar of May month - year 2020"+calendar.month(year,month))

# How to compare two dates
# < > <= >=

import datetime 
  
#two dates
dt1 = datetime.datetime(2020, 8, 10) 
dt2 = datetime.datetime(2020, 8, 14) 
  
# Comparing dates
if (dt1 > dt2):
   print("Date1 is greater tha Date2")
elif (dt1 < dt2):
   print("Date2 is greater than Date1")
else:
   print("Both the dates are equal")