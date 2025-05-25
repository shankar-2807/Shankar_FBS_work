import math  # To use the square root function
# Program to calculate the area of an equilateral triangle

side_length = int(input("Enter the side length of the equilateral triangle: "))
area = (math.sqrt(3) / 4) * (side_length ** 2)
print(f"The area of the equilateral triangle is: {area:.2f}")