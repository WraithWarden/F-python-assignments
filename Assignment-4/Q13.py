checker = int(input("Enter your maxm. no. for the pattern"))
for i in range(1, checker + 1):
    for j in range(i, 0, -1):
        print("* ", end="")
    print()
    



# can also do: 
# for i in range(1, checker + 1):
#     print("* " * i)