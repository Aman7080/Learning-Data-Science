""" 3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, 
circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them """

import math

def circle_calc(r):
    diameter = r*2
    area= round(math.pi*(r**2),3)
    circumference = round(diameter * math.pi,3)

    return area,diameter,circumference

def main():
    r = float(input("Emter radius of circle : "))
    area,diameter,circum = circle_calc(r)
    print(f"area : {area} \ndiameter : {diameter} \ncircumference : {circum}")


if __name__ == "__main__":
    main()
