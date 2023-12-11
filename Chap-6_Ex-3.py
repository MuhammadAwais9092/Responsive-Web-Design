# Chapter 6 Exercise 3: Calculator

import operator

# Function to perform addition
def add(x, y):
    return operator.add(x, y)

# Function to perform subtraction
def subtract(x, y):
    return operator.sub(x, y)

# Function to perform multiplication
def multiply(x, y):
    return operator.mul(x, y)

# Function to perform division
def divide(x, y):
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Cannot divide by zero"

# Function to calculate modulus
def modulus(x, y):
    return operator.mod(x, y)

# Function to check and return the greater number
def check_greater(x, y):
    return f"{max(x, y)} is greater"

# Function to get user input for the calculator
def get_user_input():
    try:
        # Get user input for the operation choice
        choice = input("Choose operation (1-6) or Q to quit: ").upper()
        if choice == 'Q':
            return 7, None, None  # Return a different choice value for quitting
        else:
            choice = int(choice)
            # Check if the choice is within the valid range
            if choice < 1 or choice > 6:
                raise ValueError("Invalid choice")
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            return choice, x, y
    except ValueError:
        print("Invalid input. Please enter a valid choice and numerical values.")
        return None, None, None

# Main function to run the calculator
def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number")

        # Get user input for the operation choice and numbers
        choice, x, y = get_user_input()

        if choice is None:
            continue

        if choice == 6:
            result = check_greater(x, y)
            print(f"Result: {result}")
        elif choice == 7:
            print("Exiting calculator. Goodbye!")
            break
        elif 1 <= choice <= 5:
            operations = [add, subtract, multiply, divide, modulus]
            # Perform the selected operation and print the result
            result = operations[choice - 1](x, y)
            print(f"Result: {result}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
