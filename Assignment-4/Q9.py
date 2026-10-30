vowels = {'a' : 0, 'e' : 0,  'i' : 0,  'o' : 0,  'u' : 0 }
string = input("Enter your String: ")
for i in string:
    if i.lower() in vowels:
        vowels[i.lower()] += 1

for i, j in vowels.items():
    print(f'{i} = {j}') 