# Python Program to find Sum of N  Numbers
 
number = int(input("Please Enter any Number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

print("The Sum of  Numbers from 1 to {0} =  {1}".format(number, total))