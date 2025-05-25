import cmath  # For handling complex numbers
# Program to find roots of a quadratic equation
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))
D = (b**2) - (4*a*c)

root1 = (-b + cmath.sqrt(D)) / (2*a)
root2 = (-b - cmath.sqrt(D)) / (2*a)
print(f"The roots of the quadratic equation are: {root1} and {root2}")

