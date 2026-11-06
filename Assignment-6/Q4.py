
# For the output of this file, we will use text file of Q1

def countChars(name):
    with open(name, 'r') as file:
        return len(file.read())


def countLines(name):
    with open(name, 'r') as file:
        return len(file.readlines())

def test(name):
    print(f"Number of lines: {countLines(name)}")
    print(f"Number of characters: {countChars(name)}")

if __name__ == "__main__":
    test("Q1_my_text.txt")