
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, 
              "*": multiply, "/": divide}

def calculator():
    finished = False
    num1 = float(input("What's the first number?: "))
    # display possible operations list
    for key in operations.keys():
            print(key)
        
    while finished == False:
        operation_key = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_key](num1, num2)
        print(f"{num1} {operation_key} {num2} = {answer}")
        # continue, start over or exit function
        x = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation and 'stop' to exit ")
        if x == 'n':
            finished = True
            calculator()
        elif x == 'y':
            num1 = answer
        else:
            return

calculator()