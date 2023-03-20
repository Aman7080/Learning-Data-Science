""" 
2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area.
If no shape is supplied then it should take triangle as a default shape 

area of triangle = (1/2)*base*height
area of rectangle area=length*width

"""
def calculate_area(x,y,shape="triangle"):
    """ function to return area """

    if shape == "rectangle":
        return x*y
    elif shape == "triangle":
        return (1/2)*x*y
    else:
        print("Error !!! We Calculate either triangle or rectangle")
        return None

shape = input('for which shape do you want to calculate area (triangle / rectangle) : ').lower()
x = float(input(f"Enter {'length of rectangle' if shape == 'rectangle' else 'base of triangle'}(m) : "))
y = float(input(f"Enter {'width of rectangle' if shape == 'rectangle' else 'height of triangle'}(m) : "))

print(f'Area : {calculate_area(x,y,shape)} sq m')


