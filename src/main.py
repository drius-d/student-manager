from exceptions import NotAlpha
from student import Student
import pandas as pd

def main():
    from student_loader_saver import load_students
    from student import Student
    from exceptions import NotAlpha

    # loading students from JSON file
    student_data = load_students('students.json')

    # creating dictionary. keys are names of student. values are Student class objects.
    students = {}

    for name, grades in student_data.items():
        student = Student(name, grades)

        students[name] = student

def display_menu():
    pass

def add_student(students):
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


        if student_input not in students:
            student_added = Student(student_input, grades = {})
            students[student_added.name] = student_added
            break
        else:
            print("Student already added")


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

        if student_input not in students:
            print("Student does not exist")
            continue
        
        del students[student_input]
        break

        
def view_students(students):
    current_students = {name: student.grades for name, student in students.items()}

    for name in students:
        average = students[name].calculate_average()

        current_students[name]['average'] = average

    return pd.DataFrame(current_students).T 


    # current_students = {"Alice": {'maths': 82, 'physics': 52}, ...}


def find_highest_performing_student(students):
    if not students:
        return None


    highest = 0 
    for name in students:
        average = students[name].calculate_average()

        if average > highest:
            highest = average
            highest_student = name

    return highest_student

def find_highest_subject(students):
    if not students:
        return None

    current_students = {name: student.grades for name, student in students.items()}

    subject_grades = {}

    for name, student in current_students.items():
        for subject, grade in student.items():
            if subject not in subject_grades:
                subject_grades[subject] = []

            subject_grades[subject].append(grade)

    subject_averages = {}

    for subject, grades in subject_grades.items():
        subject_averages[subject] = sum(grades) / len(grades)

    highest = 0
    for subject, average in subject_averages.items():
        if average > highest:
            highest = average
            highest_subject = subject

    return highest_subject
        

if __name__ == "__main__":
    main()
