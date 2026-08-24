from exceptions import NotAlpha
from student_pipeline import Student
import pandas as pd
from student_loader_saver import save_students

def display_screen(students):

    # keeps screen running unless save_students called
    while True:
        print("\n========================")
        print("    Student Manager")
        print("========================")

        print("\n1. View students")
        print("2. Add student")
        print("3. Remove student")
        print("4. View student")
        print("5. Add grade")
        print("6. Change grade")
        print("7. Calculate student average")
        print("8. Find highest performing student")
        print("9. Find highest average grade subject")
        print("10. Save and exit")

        print("\nTo exit the code at any point type 'cancel'")

        choice = input("\nChoose an option (Number only):")

        # checks input against number and calls specified function
        match choice:
            case "1":
                view_students(students)
            case "2":
                add_student(students)
            case "3":
                remove_student(students)
            case "4":
                view_student(students)
            case "5":
                add_grade(students)
            case "6":
                change_grade(students)
            case "7":
                calculate_student_average(students)
            case "8":
                find_highest_performing_student(students)
            case "9":
                find_highest_subject(students)
            case "10":
                save_students('students.json', students)
                break
            case _:
                print("Invalid option")
            
def add_student(students):
    # keeps code looping even when input raises an exceptions until "cancel" inputted or valid inputs inputted
    while True:
        try:
            student_input = input("Name of student:")

            # 'cancel' in case user wants to go back to menu screen
            if student_input.lower() == "cancel":
                break

            # checks if student is alphabetic. .replace() used because spaces are not considered alphabetic
            if not student_input.replace(" ", "").isalpha():
                raise NotAlpha(student_input)
        # catches exception raised and prints error messasge. restarts loop.
        except NotAlpha as e:
            print(e)
            continue

        # checks if student is not already added. creates a new Student object and then adds this object to the students array (key is name and value is Student object)
        if student_input not in students:
            student_added = Student(student_input, grades = {})
            students[student_added.name] = student_added
            print("Student added successfully")
            break
        else:
            print("Student already added")


def view_student(students):
    # keeps code looping even when input raises an exceptions until "cancel" inputted or valid inputs inputted
    while True:
        try:
            student_input = input("Name of student:")

            # 'cancel' in case user wants to go back to menu screen
            if student_input.lower() == "cancel":
                break

            # checks if student is alphabetic. .replace() used because spaces are not considered alphabetic
            if not student_input.replace(" ", "").isalpha():
                raise NotAlpha(student_input)
        # catches exception raised and prints error messasge. restarts loop.
        except NotAlpha as e:
            print(e)
            continue

        # checks if student is in the dictionary. outputs a header with the student's name. loops through each student's subject and grade, and then prints them
        if student_input in students:
            print("\n========================")
            print(f"     {student_input}")
            print("========================")

            for subject, grade in students[student_input].grades.items():
                print(f"{subject}: {grade}")
            break
        else:
            print("Student does not exist")


def remove_student(students):
    while True:
        try:
            student_input = input("Name of student:")

            if student_input.lower() == "cancel":
                break

            if not student_input.replace(" ", "").isalpha():
                raise NotAlpha(student_input)
              
        except NotAlpha as e:
            print(e)
            continue

        # checks if student is not in the dictionary and then prints error and restarts loop
        if student_input not in students:
            print("Student does not exist")
            continue

        # deletes student if in dictionary
        del students[student_input]
        print("Student removed successfully")
        break

def view_students(students):
    # creates copy of student dictionary but with values as a copy of the grades dictionary
    # current_students = {"Alice": {'maths': 82, 'physics': 52}, ...}
    current_students = {name: student.grades.copy() for name, student in students.items()}

    # for each student, calculates average and then assigns a new 'average' key this value in grades.copy
    for name in students:
        average = students[name].calculate_average()

        current_students[name]['average'] = average

    # outputs a transposed pandas dataframe
    print(pd.DataFrame(current_students).T)


def find_highest_performing_student(students):
    # checks if students dictionary is empty
    if not students:
        print("There are no students")
        return 

    # for each student calculates their average and then loops to see which student has the highest average
    highest = 0 
    for name in students:
        average = students[name].calculate_average()

        if average > highest:
            highest = average
            highest_student = name

    print("The highest performing student is", highest_student, "with average grade", highest)


def find_highest_subject(students):
    # checks if students dictionary is empty
    if not students:
        return None

    # creates copy of student dictionary but with grades dictionary instead of Student objects
    current_students = {name: student.grades.copy() for name, student in students.items()}

    # empty subject dictionary to assign subject their averages
    subject_grades = {}

    # loops through the name and grades dictionary 
    for name, student in current_students.items():
        # loops through each subject and their grade. if subject not already assigned to subject_grades create key with no value. keep appending grades to that key
        for subject, grade in student.items():
            if subject not in subject_grades:
                subject_grades[subject] = []

            subject_grades[subject].append(grade)

    subject_averages = {}

    # loops through each subject, calculates the average, and assigns the average as the value.
    for subject, grades in subject_grades.items():
        subject_averages[subject] = sum(grades) / len(grades)

    # loops through to find the subject with highest average grade
    highest = 0
    for subject, average in subject_averages.items():
        if average > highest:
            highest = average
            highest_subject = subject

    print("The highest subject by average mark was", highest_subject, "with average", highest)

def add_grade(students):
    while True:
        try:
            student_input = input("Name of student:")
            subject_input = input("Subject:")
            grade_input = (input("Grade:"))
        
            if (
                student_input.lower() == "cancel"
                or subject_input.lower() == "cancel"
                or grade_input.lower() == "cancel"
            ):
                break
            
            if (
                not student_input.replace(" ", "").isalpha() 
                or not subject_input.replace(" ", "").isalpha()
            ):
                raise NotAlpha(student_input)

            grade_input = int(grade_input)

            if not 0 <= grade_input <= 100:
                print("Grade must be between 0 and 100")
                continue

        except NotAlpha as e:
            print(e)
            continue

        except ValueError:
            print("Grade was not integer")
            continue

        if (
            student_input in students
            and subject_input not in students[student_input].grades
        ):
            students[student_input].add_grade(subject_input, grade_input)
            print("Grade successfully added")
        else:
            print("Either student does not exist or subject already added.")


def change_grade(students):
    while True:
        try:
            student_input = input("Name of student:")
            subject_input = input("Subject:")
            grade_input = (input("Grade:"))
        
            if (
                student_input.lower() == "cancel"
                or subject_input.lower() == "cancel"
                or grade_input.lower() == "cancel"
            ):
                break
            
            if (
                not student_input.replace(" ", "").isalpha() 
                or not subject_input.replace(" ", "").isalpha()
            ):
                raise NotAlpha(student_input)

            if not 0 <= grade_input <= 100:
                print("Grade must be between 0 and 100")
                continue


            grade_input = int(grade_input)

        except NotAlpha as e:
            print(e)
            continue

        except ValueError:
            print("Grade was not integer")
            continue

        if (
            student_input in students
            and subject_input in students[student_input].grades
        ):
            students[student_input].change_grade(subject_input, grade_input)
            print("Grade successfully changed")
        else:
            print("Either student or subject does not exist.")       

def calculate_student_average(students):
    while True:
        try:
            student_input = input("Name of student:")

            if student_input.lower() == "cancel":
                break

            if not student_input.replace(" ", "").isalpha():
                raise NotAlpha(student_input)
              
        except NotAlpha as e:
            print(e)
            continue

        if student_input in students:
            print("Their average is", students[student_input].calculate_average())

        else:
            print("Student does not exist")
            continue

