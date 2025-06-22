
name = input("Enter the student's name: ")
student_class = input("Enter the student's class: ")

mark1 = int(input("Enter marks of Subject 1: "))
mark2 = int(input("Enter marks of Subject 2: "))
mark3 = int(input("Enter marks of Subject 3: "))
mark4 = int(input("Enter marks of Subject 4: "))
mark5 = int(input("Enter marks of Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

print("\n--- Student Result ---")
print("Name:", name)
print("Class:", student_class)
print("Percentage:", percentage, "%")
