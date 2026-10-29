input_string = ""
while(len(input_string) < 4):
    input_string = input("Enter your string of size greater than or equal to 4: ")

new_string = input_string[:2] + input_string[-2:]

print(new_string)
