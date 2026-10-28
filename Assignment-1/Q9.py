num = int(input("Enter your 5 digit no.: "))
sum = 0
while(num):
    sum += (num % 10)
    num //= 10 
print(sum)