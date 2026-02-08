# Program: Student Grade Analyzer
# concept: Conditions in funtions.
# Description: Counts passed, failed, and distinction students using functions and lambda

def count(mark, condition):
    length = len([i for i in mark if condition(i)])
    return length

n = int(input("How many students: "))

marks = [int(input("Enter the mark: ")) for _ in range(n)]

passed = count(marks, lambda x: x >= 40)
failed = count(marks, lambda x: x < 40)
distinction = count(marks, lambda x: x >= 75)

print(f"Number of students passed = {passed}")
print(f"Number of students failed = {failed}")
print(f"Number of students got distinction = {distinction}")
