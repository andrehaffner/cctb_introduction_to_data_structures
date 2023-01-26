
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def find_max(a, b, c): return max([a, b, c])


a = float(input("Enter 1st float number: "))
b = float(input("Enter 2nd float number: "))
c = float(input("Enter 3rd float number: "))
print("The max number is", find_max(a, b, c))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def swap(a, b): return b, a


a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Before swapping: ", a, b)
a, b = swap(a, b)
print("After swapping: ", a, b)
