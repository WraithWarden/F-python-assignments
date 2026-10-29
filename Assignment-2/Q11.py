string1 = input("Enter your first string: ")

string2 = input("Enter your second string: ")

if(len(string1) < 2 or len(string2) < 2):
    print(f"Swaps can't be possible so joining without char swap answer is : {string1 + ' ' + string2}")

else:
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2]  + string2[2:]
    print(new_string1 + " " + new_string2)