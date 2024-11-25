students = {}

n = int(input("Enter the number of students: "))

for i in range(n):
     name = input("Enter the student's name: ")
     age = int(input("Enter the student's age: "))
     grade = input("Enter the student's grade: ")
     students[name] = (age, grade)

print("Student records:")
print(students)
