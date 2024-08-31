def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not possible."
    return x / y
def main():
    while True:
        print("Welcome to the Simple Calculator")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid values.")
            continue
        
        print("Choose the operation form the following:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Multiplication")
        print("d. Division")
        
        operation = input("Enter the operation number (a/b/c/d): ")
        if operation == 'a':
            result = add(number1, number2)
        elif operation == 'b':
            result = subtract(number1, number2)
        elif operation == 'c':
            result = multiply(number1, number2)
        elif operation == 'd':
            result = divide(number1, number2)
        else:
            result = "Invalid operation choice."
        
        print("Result:", result)
        continue_choice = input("Do you want to perform another calculation? (Yes/No): ").strip().lower()
        if continue_choice != 'Yes':
            print("Thank you for using Simple Calculator. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()