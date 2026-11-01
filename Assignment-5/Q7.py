s = input("Enter a phrase: ").lower()

left = 0
right = len(s) - 1

while left < right:
    if not s[left].isalnum():
        left += 1
    elif not s[right].isalnum():
        right -= 1
    elif s[left] != s[right]:
        print("Not a palindrome")
        break
    else:
        left += 1
        right -= 1
else:
    print("Palindrome")