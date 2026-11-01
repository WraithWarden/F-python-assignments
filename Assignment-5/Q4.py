testing_list = [7, 39, 11, 33, 16, 13, 78, 34, 52, 65, 70, 91, 104]

result = list(filter(lambda x: x % 13 == 0, testing_list))

print("Numbers divisible by 13 in the list are: ")
for num in result:
    print(num, end=" ")