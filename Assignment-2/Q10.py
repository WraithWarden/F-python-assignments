input_string = input("Enter your string: ")

new_string = input_string[0] + input_string[1:].replace(input_string[0], '$')
print(new_string)
