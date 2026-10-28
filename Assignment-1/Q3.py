def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


firstNumber = float(input("Enter your first no. "))
secondNumber = float(input("Enter your second no. "))

while(True):
    operator = input("Enter, either + (addition), - (subtraction), * (multiply) ,  / (divide)")
    if(operator == "+"):
        ans = add(firstNumber, secondNumber)

    elif(operator == "-"):
        ans = subtract(firstNumber, secondNumber)

    elif(operator == "*"):
        ans = multiply(firstNumber, secondNumber)
        
    elif(operator == "/"):
        if(secondNumber == 0):
            print("Cannot divide by zero")
            continue
        ans = divide(firstNumber,secondNumber)
        
    else:
        print("Enter either * , -, + or / only")
        continue

    print("Result: ", ans)
    break    
