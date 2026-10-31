str1 = input("Enter your string: ")

punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

result = ""

for char in str1:
    if char not in punctuations:
        result = result + char

print("String after removing punctuations:", result)