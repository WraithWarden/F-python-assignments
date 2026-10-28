print("finding the soln. of ax**2 + bx + c = 0")

import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# d = b**2 - 4ac
# x = (-b +- sqrt(d) ) / 2a
d = b**2 - 4*a*c
if d < 0:
    print(f"Your discriminant is {d} which is less than 0, so no solns. are possible for this eqn.")
elif a == 0:
    print(f"This is not a quadratic eqn, as ax**2 becomes 0, so your soln is unique and it is {-c/b}")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Your first soln. is {x1} and your second soln. is {x2}")
