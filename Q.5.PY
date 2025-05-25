# Program to calculate Compound Interest
P = int(input("Enter the Principal amount (P): "))
T = int(input("Enter the Time (T) in years: "))
R = int(input("Enter the Rate of interest (R) per annum: "))

amount = P * (1 + R / 100) ** T
CI = amount - P

print(f"Compound Interest = {CI}")
print(f"Total Amount = {amount}")

