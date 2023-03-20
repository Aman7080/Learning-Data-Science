""" 
3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

*
**
***

if input is 4 then it should print

*
**
***
****

"""
import sys
def print_pattern(num:int):
    for i in range(num):
        for j in range(i+1):
            sys.stdout.write('*')
        print()


print_pattern(3)