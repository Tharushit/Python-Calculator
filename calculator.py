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
    else:
        print("Unrecognized operation")
        return None