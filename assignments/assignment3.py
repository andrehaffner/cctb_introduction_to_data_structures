
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print("The factorial of negative numbers is not defined")
else:
    for i in range(1, number+1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Code 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

number = int(input("Enter a number: "))
print(str(number)[::-1])
