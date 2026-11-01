num = int(input("Enter your n to find sum of natural no.s: "))
def sum_n(num: int):
    if num <= 0: 
        return 0
    return num + sum_n(num - 1)
print(sum_n(num))