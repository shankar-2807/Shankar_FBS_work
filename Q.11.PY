import math  # For the value of pi and other math functions

# Program to calculate the area and circumference of a circle
radius = int(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")

