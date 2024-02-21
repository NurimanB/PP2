"""
Area of regular polygon: A=(n*a^2)/(4*tan(pi/4)) 
where, 
n - number of sides
a - length of a side
"""
import math

def Polygon(n, a):
    return math.floor((n*(a**2))/(4*math.tan(math.pi/4)))

n = int(input("Input number of sides: "))  
a = int(input("Input the length of a side: "))

print("The area of the polygon is: ", Polygon(n, a))