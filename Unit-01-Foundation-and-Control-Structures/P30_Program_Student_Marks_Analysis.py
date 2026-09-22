n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    marks.append(float(input("Enter marks: ")))

average = sum(marks) / n
highest = max(marks)
lowest = min(marks)
passed = 0
failed = 0
above75 = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1

    if mark > 75:
        above75 += 1

print("Class Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Passed:", passed)
print("Failed:", failed)
print("Above 75%:", above75)
