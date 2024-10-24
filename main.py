# Area of Sphere Program

def sphere_area(radius):
    """
    Calculate the surface area of a sphere given its radius.
    
    Formula: 4 * π * r^2
    """
    pi = 3.142
 
    area = 4 * pi * r ** 2
    return area


r = float(input("Enter radius of the sphere: "))
print("The area of the sphere:", sphere_area(r))




