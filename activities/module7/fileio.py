
try:
    # Getting inputs
    file = open(input("Enter source file name: "))
    destination = input("Enter destination file: ")

    # Defining lines and empty new text
    lines = [line.rstrip() for line in file]
    new_text = ""
    header = True

    # Reading/Writing lines
    for line in lines:
        # If header pass the line and add new header
        if header:
            new_text += "Name Average\n"
            header = False
        # Else add name and average to new line
        else:
            values = line.split(" ")
            name = values[0]
            average = ((float(values[1]) + float(values[2]) + float(values[3]) + float(values[4])) / 4)
            new_text += name + " " + str(average) + "\n"

    # Saving new file
    new_file = open(destination, "x")
    new_file.write(new_text)
    new_file.close()
    print(new_text)
except FileNotFoundError:
    print("- Error: file not found!")
