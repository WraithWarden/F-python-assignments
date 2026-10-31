for i in range(1, 11):
    print(f"{i} |", end="\t")

    for j in range(1, 11):
        print(f"{i * j}", end="\t")

    print()