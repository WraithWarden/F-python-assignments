input_string = ""
while(len(input_string) < 3):
    input_string = input("Enter string of size greater than or equal to 3")

new_string = ""
if input_string.endswith('ing'):
    new_string = input_string + 'ly'
else:
    new_string = input_string + 'ing'

print(new_string)
