import math

rad = float(input("Give the radius of the cylinder: "))
depth = float(input("Give the depth of the cylinder: "))
c_area = math.pi*(rad**2)
c_volume = c_area*depth
print("Total volume of cylinder is:",round(c_volume,3))