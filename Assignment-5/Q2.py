num = int(input())
fib0, fib1 = 0, 1
if num >= 1:
    print(fib0, end=" ")

if num >= 2: 
    print(fib1, end= " ")

for i in range(2, num):
    fib_next = fib0 + fib1 
    print(fib_next, end= " ")
    fib0 = fib1
    fib1 = fib_next



# 0 1 1 2