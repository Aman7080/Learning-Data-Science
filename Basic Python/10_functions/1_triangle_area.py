""" 
1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
 area of triangle = (1/2)*base*height 
"""

def calculate_area(base,height):
    """ function to return area of triangle """
    return (1/2)*base*height

base = float(input("Enter base of triangle(m) : "))
height = float(input("Enter height of triangle(m) : "))

print(f'Area of triangle : {calculate_area(base,height)} sq m')


