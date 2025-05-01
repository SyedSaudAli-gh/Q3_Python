# Create a python program capable of greeting you with Good Morning,
# Good Afternoon and Good Evening. Your program should use time module
# to get the current hour. Here is a sample program and documentation link
# for you;

import time 

timestamp = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))


if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
else:
    print("Good Evening!")

print(f"Current time is: {timestamp}")