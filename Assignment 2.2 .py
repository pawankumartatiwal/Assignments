# Taking student details
name = input("Enter the student's name: ")
student_class = input("Enter the student's class: ")

mark1 = int(input("Enter marks of Subject 1: "))
mark2 = int(input("Enter marks of Subject 2: "))
mark3 = int(input("Enter marks of Subject 3: "))
mark4 = int(input("Enter marks of Subject 4: "))
mark5 = int(input("Enter marks of Subject 5: "))

# Calculating total and percentage
total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

# Grade calculation
if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'

# result
print("\n--- Student Result ---")
print("Name:", name)
print("Class:", student_class)
print("Percentage:", percentage, "%")
print("Grade:", grade)
