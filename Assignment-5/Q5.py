num = int(input("Enter no. of terms: "))

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)
if num <= 0:
    print("Enter a valid +ve no.")
else:
    for i in range(num):
        print(fib(i), end=" ")