marks = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))
    marks[name] = mark

print("Student Marks:")
for name, mark in marks.items():
    print(name, ":", mark)
