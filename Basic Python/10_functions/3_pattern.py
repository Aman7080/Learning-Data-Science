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

def print_pattern(num:int):
    for i in range(num):
        for j in range(i+1):
            print('*',end="")
        print()

num = int(input("Enter a Number : "))
print_pattern(num)