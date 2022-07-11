# To get current date and time we need to use the dateime library
from datetime import date, datetime

# The now function returns current date and time
today = datetime.now()

# use day, month, year, hour, minute, second functions 
# to display only part of the dateAll these functions return integers 
# Convert them to strings before concatenating them to another string

print('Day: ' + str(today.day))
print('Month: ' + str(today.month)) 
print('Year: ' + str(today.year))
print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))