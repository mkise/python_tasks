import random

def user_input():
    """
    Function to get user input of two numbers and an operator.
    Returns the numbers and operator.
    """
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            op = input("Enter an operator of choice (+, -, *, /): ")

            if op not in ['+', '-', '*', '/']:
                print('Invalid operator')
                print('Please enter a valid operator.')
                continue

            return num1, num2, op

        except ValueError:
            print('Invalid input')
            print('Please enter valid numeric values.')
            continue


def calculate(num1, num2, op):
    """
    Function to perform the calculation based on the operator.
    Returns the result of the calculation.
    """
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '/':
            return num1 / num2
        elif op == '*':
            return num1 * num2
        else:
            raise ValueError('Invalid operator')
        # Catch any division by zero errors and print an error message
    except ZeroDivisionError:
        return 'Can\'t divide by zero'


def write_equation_to_file(equation, result):
    """
    Function to write equations and results to a file.
    """
    if result is not None:
        with open("equations.txt", "a") as f:
            f.write(f"{equation} = {result}\n")


def get_file(filename):
    """
    Function to read equations from a file and evaluate them.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                equation = line.strip()
                try:
                    result = eval(equation)
                    print(f'{equation} = {result}')
                except (ZeroDivisionError, SyntaxError, NameError):
                    print(f'{equation}')
    except FileNotFoundError:
        print('File not found')


choice = input('Would you like to use your own file for calculations or enter a number?\nFile (F)\nNumber (N)?: ').lower()

if choice == 'n':
    while True:
        # Get user input for two numbers and an operator
        num1, num2, op = user_input()
        # Perform the calculation based on the operator
        result = calculate(num1, num2, op)
        print(f'Answer: {result}\n')
        # Write the equation and result to the file
        write_equation_to_file(f"{num1} {op} {num2}", result)

    # Ask the user if they want to continue or quit
        choice = input("Enter 'C' to continue with another calculation or 'Q' to quit: ").lower()
        if choice == 'q':
            break
# If the user chooses to use a file
elif choice == 'f':
    try:
        file_name = input('Please enter the name of the file: ')
        get_file(file_name)
    except FileNotFoundError:
        print('File not found')

# If the user enters an invalid choice
else:
    print('Invalid option')

