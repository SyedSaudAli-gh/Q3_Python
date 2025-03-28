# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

DAYS_IN_YEAR: int = 365
HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60
SECONDS_IN_MINUTE: int = 60


print(f"There are {DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE} seconds in a year!")    
    
