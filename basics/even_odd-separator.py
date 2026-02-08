# Program: Odd and Even Number Separator
# Concept: Lists, loops, conditionals
# Description: Separates given numbers into odd and even lists

count = int(input("Enter how many numbers you want to enter: "))
odd = []
even = []

for i in range(count):
    value = int(input("Enter the number: "))
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

print("\nResults:")
print("Even numbers:", even)
print("Odd numbers:", odd)
