# Program: Positive, Negative and Zero Counter
# Concept: Using Lists and list comprehension
# Description: Counts positive, negative and zero values from user input

count = int(input("Enter number of digits: "))

number = [int(input("Enter the number: ")) for i in range(count)]

positive = [val for val in number if val > 0]
pcount = len(positive)

negative = [val for val in number if val < 0]
ncount = len(negative)

zero = [val for val in number if val == 0]
zcount = len(zero)

print(f"Count of positive: {pcount}")
print(f"Count of negative: {ncount}")
print(f"Count of zeros: {zcount}")
