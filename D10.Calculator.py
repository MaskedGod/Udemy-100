
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return int(n1 / n2)

operations = {"+": add, "-": subtract, 
              "*": multiply, "/": divide}

num1 = int(input("What's the first number?: "))
# display possible operations list
for key in operations.keys():
    print(key)
operation_key = input("Pick an operation from the list above: ")
num2 = int(input("What's the second number?: "))
answer = operations[operation_key](num1, num2)
print(f"{num1} {operation_key} {num2} = {answer}")