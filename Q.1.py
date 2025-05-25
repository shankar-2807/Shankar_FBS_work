# Program to calculate percentage based on marks of 5 subjects

Marathi = int(input("Enter marks subject1: "))
Math = int(input("Enter marks subject2: "))
English = int(input("Enter marks subject3: "))
Science = int(input("Enter marks subject4: "))
History = int(input("Enter marks subject5: "))

Totalmarks = Marathi + Math + English + Science + History
percentage = (Totalmarks / 500)* 100
print("Total marks :", Totalmarks,"/500")
print("percentage:", percentage, "%")
