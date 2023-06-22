logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# calculator
from art import logo
print(logo)


def sum(num1, num2):
    return num1 + num2


def product(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2


def subtraction(num1, num2):
    return num1 - num2


num1 = float(input("Enter the first number: "))
continue_calculation = True

while continue_calculation:
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Multiplication (*)")
    print("3. Division (/)")
    print("4. Subtraction (-)")

    operation = input("Pick an operation (1-4): ")

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        continue

    num2 = float(input("Enter the second number: "))

    if operation == '1':
        result = sum(num1, num2)
        operator = "+"
    elif operation == '2':
        result = product(num1, num2)
        operator = "*"
    elif operation == '3':
        try:
            result = division(num1, num2)
            operator = "/"
        except ZeroDivisionError as e:
            print("Error:", str(e))
            continue
    else:
        result = subtraction(num1, num2)
        operator = "-"

    print(f"{num1} {operator} {num2} = {result}")

    decision = input(
        f"Press 'n' to end the calculation or any other key to continue with {result}: ")

    if decision == 'n':
        continue_calculation = False
    else:
        num1 = result

print("Calculation ended.")
