# Program: Number Analyzer
# Concept: Loops, conditionals, basic arithmetic
# Description: Calculates sum, maximum, minimum, and average of given numbers

count = int(input("Enter how many numbers you want to analyze: "))
number = int(input("Enter a number: "))
total = number
min_val = number
max_val = number

for i in range(1, count):
    number = int(input("Enter a number: "))
    total += number
    if number > max_val:
        max_val = number
    if number < min_val:
        min_val = number

average = total / count

print("\nResults:")
print("Sum:", total)
print("Maximum:", max_val)
print("Minimum:", min_val)
print("Average:", average)
