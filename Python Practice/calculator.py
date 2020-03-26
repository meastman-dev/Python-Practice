def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def divide(x,y,error_message=''):
    if y == 0:
        return error_message
    else:
        return x/y
def multiply(x,y):
    return x * y
def calculate():
    operation = ''
    print("After entering 2 numbers, you will be prompted to enter an operation.")
    while operation != 'quit':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter the second number: "))
        print()
        print("1 Add")
        print("2 Subtract")
        print("3 Multiply")
        print("4 Divide")
        print("'Quit' to close")
        print()
        operation = input("Enter an operation: ")
        if operation == '1':
            print(add(num1,num2))
        elif operation == '2':
            print(subtract(num1, num2))
        elif operation == '3':
            print(multiply(num1, num2))
        elif operation == '4':
            error_message = 'ERROR: Cannot divide by 0'
            print(divide(num1, num2, error_message))
        elif operation == 'Quit':
            print("Exiting calculator")
            break;
        else:
            print("Please enter an operation choice.")
        print()
calculate()

