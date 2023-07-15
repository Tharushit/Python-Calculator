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
  if (choice == '#'):
    return -1
  elif (choice == '$'):
    return 0
  elif choice == '?':
        history()
        return None
  elif (choice in ('+','-','*','/','^','%')):
    while (True):
      num1s = str(input("Enter first number: "))
      print(num1s)
      if num1s.endswith('$'):
        return 0
      if num1s.endswith('#'):
        return -1
        
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    while (True):
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
      if num2s.endswith('#'):
        return -1
      try:  
        num2 = float(num2s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    result = 0.0
    last_calculation = ""
    if choice == '+':
      result = add(num1, num2)
    elif choice == '-':
      result = subtract(num1, num2)
    elif choice == '*':
      result = multiply(num1, num2)
    elif choice == '/':
      result =  divide(num1, num2)
    elif choice == '^':
      result = power(num1, num2)
    elif choice == '%':
      result = remainder(num1, num2)
    elif choice == '?':
      result = history()
    else:
      print("Something Went Wrong")
      
    last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result)
    previous_operations.append(last_calculation)
    print(last_calculation )
    
    
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
    print("9.History  : ? ")

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