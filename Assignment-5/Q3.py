num = int(input("Enter the no. of terms: "))

power_of_2 = lambda x: 2 ** x

for i in range(num):
    print(f'2^{i} = {power_of_2(i)}')