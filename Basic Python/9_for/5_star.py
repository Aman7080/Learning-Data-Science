""" 5. Write a program that prints following shape

            *
            **
            ***
            ****
            *****
"""
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()