# Program to convert days into years, weeks, and days.

days = int(input("Enter the number of days: "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
remaining_days = remaining_days % 7

print(f"{days} days is equivalent to:")
print(f"{years} years, {weeks} weeks, and {remaining_days} days.")

