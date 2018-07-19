import time
import datetime

print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: ", datetime.datetime.now()
print "Or like this: ", datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")

print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%W")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of the week: ", datetime.date.today().strftime("%A")

print "Solution that gives me days, no time"
from datetime import date
age = date.today() - date(1981, 3, 31)
age_years = age / 365
print(age.days)
print age_years

print "Solution that gives me # of days and time"
#year, month, day, hour, minute, second
my_bday = datetime.datetime(1981, 3, 31, 10, 15, 0)
bday_days = (datetime.datetime.now()  - my_bday)


bday_years = bday_days.days / 365

print "I am %s years old!" % bday_years
