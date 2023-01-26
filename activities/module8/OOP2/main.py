from student_management import *
from student import Student
from time import sleep


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Raw data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

options = "\n\n\t1. Add student\n\t2. Update student\n\t3. Delete by ID\n\t4. Find by name\n\t5. sort by gpa" \
          "\n\t6. Sort by name\n\t7. Sort by ID\n\t8. Print Students\n\t0. Exit"
line = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
students = [Student("André", "Male", 21, 8.2, 9.1, 7.5), Student("Leonardo", "Male", 9, 10, 9.1, 7.2)]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Program ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

while True:
    try:
        # ~~~~~ Getting user input ~~~~~ #
        sleep(1)
        print(line)
        print("\nRunning program...")
        sleep(1)
        chosen_option = int(input("\nOptions:" + options + "\n\nChoose one: "))

        # ~~~~~ Executing task related to input ~~~~~ #
        if chosen_option == 1:
            add_student(students)
        elif chosen_option == 2:
            update_student(students)
        elif chosen_option == 3:
            delete_by_id(students)
        elif chosen_option == 4:
            find_by_name(students)
        elif chosen_option == 5:
            sort_by_gpa(students)
        elif chosen_option == 6:
            sort_by_name(students)
        elif chosen_option == 7:
            sort_by_id(students)
        elif chosen_option == 8:
            print_students(students)
        elif chosen_option == 0:
            print("Thank you for using our app!")
        else:
            print("Wrong command!")

    # ~~~~~ If user inputs string ~~~~~ #
    except ValueError:
        print("\n\t- Input error: only numbers accepted!\n")
