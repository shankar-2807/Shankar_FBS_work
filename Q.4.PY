# Program to calculate Simple Interest
P = int(input("Enter the Principal amount (P): "))
T = int(input("Enter the Time (T) in years: "))
R = int(input("Enter the Rate of interest (R) per annum: "))

SI = (P * T * R) / 100
print(f"Simple Interest = {SI}")

