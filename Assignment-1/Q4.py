import math
num = float(input("Enter your no. to find the square root of it: "))
ans_using_lib = math.sqrt(num)
print(f'Sqaure root of {num} using the math lib. is {ans_using_lib}')

ans_using_op = num ** (1/2)
print(f"Sqaure root of {num} using the '**' operator is {ans_using_op}")
