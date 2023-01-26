
nums = list()
while True:
    try:
        num = int(input("Enter a positive integer number: "))
        if num < 0:
            print("- Cannot enter a negative number!\n- Shutting down...")
            break
        elif num > 0:
            nums.append(num)
        else:
            squares = [x**2 for x in nums]
            print("\nUser entered:", nums)
            print("The square of the given numbers:", squares)
            break
    except ValueError:
        print("- Error: enter an integer!")
        continue
