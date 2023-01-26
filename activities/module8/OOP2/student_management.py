from student import Student
from time import sleep


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Add student ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def add_student(students):
    name = input("\n\tStudents name: ")
    gender = input("\tStudents gender: ")
    while True:
        try:
            age = int(input("\tStudents age: "))
            chemistry = float(input("\tStudents chemistry: "))
            physis = float(input("\tStudents physis: "))
            math = float(input("\tStudents math: "))
            break
        except ValueError:
            print("\n\n\tAge must be an int, and grades must be floats!\n")
    print(f"\n\tStudent {name} added!")
    students.append(Student(name, gender, age, math, physis, chemistry))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Update student ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def update_student(students):
    while True:
        try:
            id = int(input("\n\tID: "))
            a = 0
            for student in students:
                if student.id == id:
                    print("\n\tOld values:")
                    print("\t\tName:", student.name)
                    print("\t\tGender:", student.gender)
                    print("\t\tAge:", student.age)
                    print("\t\tMath:", student.mathematics)
                    print("\t\tPhysis:", student.physis)
                    print("\t\tChemistry:", student.chemistry)
                    print("\n\tEnter new values: ")
                    name = input("\t\tName: ")
                    gender = input("\t\tGender: ")
                    while True:
                        try:
                            age = int(input("\t\tAge: "))
                            chemistry = float(input("\t\tChemistry: "))
                            physis = float(input("\t\tPhysis: "))
                            math = float(input("\t\tMath: "))
                            break
                        except ValueError:
                            print("\t\tAge must be an int, and grades must be floats!\n")
                    student.name = name
                    student.age = age
                    student.gender = gender
                    student.chemistry = chemistry
                    student.physis = physis
                    student.math = math
                    a = 1
                    print("\n\t\tUpdated student!")
                    break
            if a == 0:
                print("\n\tStudent not found!")
            break
        except ValueError:
            print("\n\tID must be integer!")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Delete by ID ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def delete_by_id(students):
    while True:
        try:
            id = int(input("\n\tID: "))
            a = 0
            for student in students:
                if student.id == id:
                    students.remove(student)
                    a = 1
                    print("\n\tStudent deleted!")
            if a == 0:
                print("\n\tStudent not found!")
            break
        except ValueError:
            print("\n\tID must be integer!")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Find by name ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def find_by_name(students):
    name = input("\n\tName: ")
    a = 0
    for student in students:
        if student.name == name:
            print("\n\tStudent found:")
            print("\t\tID:", student.id)
            print("\t\tName:", student.name)
            print("\t\tAge:", student.age)
            print("\t\tGender:", student.gender)
            print("\t\tMath:", student.mathematics)
            print("\t\tPhysis:", student.physis)
            print("\t\tChemistry:", student.chemistry)
            a = 1
            break
    if a == 0:
        print("\n\tStudent not found!")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Sort by GPA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def sort_by_gpa(students):
    order = dict()
    for student in students:
        order[student.gpa] = str(student.id) + "//" + student.name
    order = dict(sorted(order.items()))
    print("\n\tPrinting students by gpa:")
    for key, value in order.items():
        sleep(1)
        print("\n\t\tName:", value.split("//")[1])
        print("\t\tID:", value.split("//")[0])
        print("\t\tGPA:", key)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Sort by name ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def sort_by_name(students):
    order = dict()
    for student in students:
        order[student.name] = str(student.gpa) + "//" + str(student.id)
    order = dict(sorted(order.items()))
    print("\n\tPrinting students by name:")
    for key, value in order.items():
        sleep(1)
        print("\n\t\tName:", key)
        print("\t\tID:", value.split("//")[1])
        print("\t\tGPA:", value.split("//")[0])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Sort by ID ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def sort_by_id(students):
    order = dict()
    for student in students:
        order[student.id] = str(student.gpa) + "//" + student.name
    order = dict(sorted(order.items()))
    print("\n\tPrinting students by ID:")
    for key, value in order.items():
        sleep(1)
        print("\n\t\tName:", value.split("//")[1])
        print("\t\tID:", key)
        print("\t\tGPA:", value.split("//")[0])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Print students ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def print_students(students):
    print("\n\tPrinting students:")
    for student in students:
        print("\n\t\tName:", student.name)
        print("\t\tID:", student.id)
        print("\t\tAge:", student.age)
        print("\t\tGender:", student.gender)
        print("\t\tMath:", student.mathematics)
        print("\t\tPhysis:", student.physis)
        print("\t\tChemistry:", student.chemistry)