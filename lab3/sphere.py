#V=4/3 pi*r^3
import math

def volume(radius):
    vol = 4/3 * math.pi * pow(radius, 3)
    print(vol)

radius = int(input("Enter a radius of sphere: "))
volume(radius)