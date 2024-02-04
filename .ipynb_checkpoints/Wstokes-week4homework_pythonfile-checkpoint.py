#Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month name form that variable.
import datetime as dt
now = dt.datetime.now()
print(now)

#Write a simple function that takes 2 parameters -- a first name and a day name.
#Set a default value for the day name of Sunday.
#Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.
def hello(first_name,last_name):
    print(f"Hi, {first_name}! Happy {last_name}!")
    print(f"Hi, {first_name}!")

hello("John Snow","Sunday")

#Write a block of code to handle one of the most common Python exception errors. Select one of the common errors from the curriculum section on Python Exception handling. Have your code example uses the try,except, else, and finally components.
try: 
    print("try")
except:
    print("except")
else:
    print("else")
finally:
    print("fianlly")