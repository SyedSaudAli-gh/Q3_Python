# Project 6: Countdown Timer Python Project

import time

def countdown(t:int):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
        
    print("Timer Completed!")
    
user_input:int = int(input("Enter the timer in seconds: ")) 

countdown(int(user_input))