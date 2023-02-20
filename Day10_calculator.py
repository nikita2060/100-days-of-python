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
def sum(num1,num2):
  return (num1+num2)
def product(num1,num2):
  return (num1*num2)
def division(num1,num2):
  return (num1/num2)
def subtraction(num1,num2):
  return (num1-num2)
num1=float(input("Enter first number\n"))
while True:
  operators={"+":sum,
            "*":product,
            "/":division,
            "-":subtraction }
  for keys in operators:
    print(keys)
  sign=input("Pickup an operation sign from above:\n")
  calculation=operators[sign]
  num2=float(input("Enter second number\n"))
  result=calculation(num1,num2)
  print(f"{num1}{sign}{num2}={result}")
  if input(f"Type n for ending calculation and y for continuing calculation with {result} ")=='y':
    num1=result
  else:
    break
 
