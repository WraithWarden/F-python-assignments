max_stars = int(input("Enter no. of maxm. stars in the middle row: "))


total_rows = (2 * max_stars) - 1

for i in range(1, total_rows + 1):
    # Calculate stars: counts up to max_stars, then mirrors back down
    if i <= max_stars:
        stars = i 
    else:
        stars = (2 * max_stars) - i
    print("* " * stars)
