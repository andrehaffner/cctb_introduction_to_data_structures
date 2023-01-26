
# TypeError = data type of an object in an operation is inappropriate
try:
    age = int(input("Enter yout age: "))
    print(f"In ten years you'll have {age+10} years old.")
except TypeError:
    print("- Error: you must enter a number!")


# IndexError = index not valid to that object
name = input("Enter your name: ")
try:
    print("The 10th char of your name is:", name[10])
except IndexError:
    print("Your name is too short for this algorithm :(")
