# Program: Menu Driven Calculator
# Concept: Functions,Recursion
# Description: Performs basic arithmetic operations using functions and a menu

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting...")
        break

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(x, y))
    elif choice == 2:
        print("Result:", subtract(x, y))
    elif choice == 3:
        print("Result:", multiply(x, y))
    elif choice == 4:
        result = divide(x, y)
        if result is None:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", result)
    else:
        print("Invalid choice, try again")
