import datetime
from datetime import timedelta

month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year: "))


days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# First day of the month
d = datetime.date(year, month, 1)

# Get month name and print title
month_name = d.strftime("%B")
title = month_name + " " + str(year)
print()
print(title.center(30), end='\n\n')

# Print day 
for x in days:
    print(x, end=' ')
print()

# Find out the weekday index for the 1st (Sunday = 0)
start_day_index = (d.weekday() + 1) % 7


print("    " * start_day_index, end='')

#last day
if month == 12:
    next_month = datetime.date(year + 1, 1, 1)
else:
    next_month = datetime.date(year, month + 1, 1)
last_day = (next_month - timedelta(days=1)).day

# All days of the month
for day in range(1, last_day + 1):
    print(f"{day:>3}", end=' ')
    
    
    current_date = datetime.date(year, month, day)
    if current_date.weekday() == 5:  # Saturday
        print() 

print() 

'''
Enter a month (1-12): 6
Enter a year: 2025

          June 2025

Sun Mon Tue Wed Thu Fri Sat
  1   2   3   4   5   6   7
  8   9  10  11  12  13  14
 15  16  17  18  19  20  21
 22  23  24  25  26  27  28
 29  30

'''