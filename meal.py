#Filename: meal.py
from decimal import *
def main():
    currentTime = convert("What time is it? ")
    processMealTime(currentTime)
def convert(prompt):
    currentTime = input(prompt)
    hours, minutes = currentTime.split(":")
    hours = Decimal(hours)
    minutes = Decimal(minutes)
    convertedTime =  Decimal(hours + minutes/60)
    return convertedTime
def processMealTime(t):
   
    if (7.0 <= t <= 8.0):
        print("breakfast time")
    elif 12.0 <= t <= 13.0:
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")
    else:
        print("")  
if __name__ == "__main__":
    main()