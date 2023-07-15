previous_operations=[]

def add(a, b):
    return float(a + b)

def subtract(a, b):
    return float(a - b)

def multiply(a, b):
    return float(a * b)

def divide(a, b):
    if b != 0:
        return float(a / b)
    else:
        print("float division by zero")
        return None
    
def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def history():
    if len(previous_operations) == 0:
        print("No past calculations to show")
    else:
        for i, operation in enumerate(previous_operations, start=1):
            print(f"{operation}")


def select_op(choice):
    if choice == '+':
        return add
    elif choice == '-':
        return subtract
    elif choice == '*':
        return multiply
    elif choice == '/':
        return divide
    elif choice == '^':
        return power
    elif choice == '%':
        return remainder
    elif choice == '#':
        return None
    elif choice == '$':
        print("Resetting")
        return None
    elif choice == '?':
        history()
        return None
    
    else:
        print("Unrecognized operation")
        return None
    

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if choice == '#':
        print("Done. Terminating")
        break

    elif choice == '$':
        print("Resetting")
        continue
    
    num1 = input("Enter first number: ")
    if num1 == '#' or num1 == '':
        print(num1)
        print("Done. Terminating")
        break
    
    try:
        num1 = int(num1)
        print(num1)
    except ValueError:
        print(num1)
        continue

    num2 = input("Enter second number: ")
    if num2 == '#' or num2 == '':
        print(num2)
        print("Done. Terminating")
        break

    try:
        num2 = int(num2)
        print(num2)
    except ValueError:
        print(num2)
        continue


    op_func = select_op(choice)
    if op_func is None:
        break

    result = op_func(num1, num2)
    print(f"{num1:.1f} {choice} {num2:.1f} = {result}")