def is_pangram(s):
    s = s.lower()

    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in s:
            return False

    return True


s = input("Enter a sentence: ")

if is_pangram(s):
    print("Pangram")
else:
    print("Not a Pangram")