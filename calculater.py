# the calculator app
def calculator(num1, op ,num2):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)

def get_number1():
    while True:
        try:
            num1 = int(input("Enter 1st number: "))
            return num1
        except ValueError:
            print("Please enter a valid number")

def get_number2():
    while True:
        try:
            num2 = int(input("Enter 2nd number: "))
            return num2
        except ValueError:
            print("Please enter a valid number")

def operation():
    op = input('Enter an operation(+ , - , * , /): ')
    while not op == "+" and not op == "-" and not op == "*" and not op == "/":
        print('Enter a valid operation')
        op = input('Enter an operation(+ , - , * , /): ')
    return op

calculator(get_number1(), operation() ,get_number2())
