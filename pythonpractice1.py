#This code takes your name and age and tells you how many years are left before you are 100.
#It also gives you the year at which you will be 100/

from datetime import *

date = datetime.today().year
stringdate = str(date)
name = (input("What is your name: "))
age = int(input("How old are you: "))
yearsleft = (100 - age)
laterdate = date+yearsleft
stringlaterdate = str(laterdate)
stringyearsleft = str(yearsleft)
lines = int(input("How many times would you like to print this: "))
for i in range(lines):
        print("Hi " + name + ", you have " + stringyearsleft + " years left unt$
        print("It is currently " + stringdate + " and it will be " + stringlate$
        print("\n")
