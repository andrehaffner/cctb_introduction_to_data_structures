from math import sqrt

print("\nSolve quadratic equation!\nax2 + bx + c = 0")

a = b = c = 0

while a == 0 or b == 0 or c == 0:
    print("a, b and c cannot be 0!")
    try:
        a = float(input("\nEnter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        break
    except ValueError:
        print("\nYour inputs must be real numbers!")
        continue

delta = b**2-4*a*c
if delta > 0:
    x1 = (-1*b + sqrt(delta))/2*a
    x2 = (-1*b - sqrt(delta))/2*a
    if x1 == x2:
        print(f"\nResult:\nx1 = x2 = {x1}")
    else:
        print(f"\nResult:\nx1 = {x1}\nx2 = {x2}")
else:
    print("\nResult:\nThere are no real solutions")
