def add(a: float , b: float):
    return a + b
def sub(a: float , b: float):
    return a - b
def mul(a: float , b: float):
    return a * b
def div(a: float , b: float):
    return a / b


checker = True

while(checker):
    print(
        """
        Select operations: 
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Exit
        """)
    checker = int(input("Enter choice (1/2/3/4/5): "))
    if checker == 5:
        break
    elif checker > 5 or checker < 1:
        print("Please enter a valid input between 1 to 5")
        print()
        

    else:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        if checker == 1:
            print(add(first, second))
        elif checker == 2:
            print(sub(first, second)) 
        elif checker == 3: 
            print(mul(first, second))
        else:
            while second == 0:
                print("Cannot divide by 0")
                second = float(input("Enter second number not equal to 0: "))

            print(div(first, second))


