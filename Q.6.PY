# Program to find the third angle of a triangle.

# Program to find the third angle of a triangle
angle1 = int(input("Enter first angle of the triangle: "))
angle2 = int(input("Enter second angle of the triangle: "))
angle3 = 180 - (angle1 + angle2)

sum_of_triangle_angles_= 180
sum_of_triangle_angles = angle1 + angle2 + angle3
print(f'The third angle of the triangle is: {angle3} degrees')


