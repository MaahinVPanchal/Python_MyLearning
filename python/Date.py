# Python DateTime:-
# To work with Dates in Python, import a module datetime.

# datetime module class :--
# class datetime.date ==> Naive date assuming the current Gregorian calendar always was
# class datetime.time ==> Time
# class datetime.datetime ==> Combination of date and time
# class datetime.timedelta ==> Duration expressing the difference between two date, time or datetime
# class datetime.tzinfo ==> Used by datetime and time classes to provide a customizable notion of time adjustment.

# Get the current date and time
import datetime

res = datetime.datetime.now()
print("Current Date and Time = ",res)

# Get Today’s Date
from datetime import date
res1 = date.today()
print("Getting today's date: ",res1)

# Get the weekday (short)
import datetime
 
#date1 and date2
date1 = datetime.datetime.now()
date2 = datetime.datetime(2020, 4, 25) 
 
print("Date1 = ",date1)
print("Date1 weekday = ",date1.strftime("%a"))

print("Date2 = ",date2)
print("Date2 weekday = ",date2.strftime("%a"))

# Get the weekday (complete)
# %A format code
print("Date2 weekday in complete = ",date2.strftime("%A"))

# Get the weekday as a number 
print("Date2 weekday as number = ",date2.strftime("%w"))

# Get the day of month
print("Date2 day of month = ",date2.strftime("%d"))

# Get the month name (short)
print("Date2 month name = ",date2.strftime("%b"))

# Get the month name (complete)
print("Date2 month name = ",date2.strftime("%B"))

# Display the month as a number
print("Date2 month as number = ",date2.strftime("%m"))

# Display year (short)
print("Date2 year (without century) = ",date2.strftime("%y"))

# Display year (complete)
print("Date2 year (with century) = ",date2.strftime("%Y"))

# Display hour in 24-hour format
print("Date1 hour (24 hour format) = ",date1.strftime("%H"))

# Display hour in 12-hour format 
print("Date1 hour (12 hour format) = ",date1.strftime("%I"))

# Display whether the date is AM/PM
print("Date1 time in AM/PM = ",date1.strftime("%p"))

# Display Day number (001-366) of year
print("Date1 day number(001-336) = ",date1.strftime("%j"))

# Get the week number of year
print("Date1 week number of year = ",date1.strftime("%U"))