# Student marks record
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(name + "'s marks: " + str(student_marks[name]))
else:
    print("Student not found.")