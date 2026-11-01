def overlapping(list1, list2):
    set2 = set(list2)

    for x in list1:
        if x in set2:
            return True

    return False


a = [1, 6, 10, 4, 11, 17, 20, 4, 10, 8]
b = [5, 6, 3, 7, 21, 34, 4, 10, 17, 1]

print(overlapping(a, b))