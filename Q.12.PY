import math  # For the value of pi and other math functions

# Program to calculate the volume of a sphere
radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * (radius ** 3)
print(f"The volume of the sphere is: {volume:.2f}")

