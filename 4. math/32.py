import math

radius = float(input("Enter the radius of the cylinder: "))
depth = float(input("Enter the depth of the cylinder: "))

area = math.pi*radius**2
volume = area*depth

print("your circle's volume is ",round(volume, 3))

