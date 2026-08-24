import json
from student_pipeline import Student

# Defining function to load
def load_students(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Defining function to save
def save_students(filename, students):
    # Takes dictionary with {'name': <student.Student object at {location}>, ...} and turns it back into a dictionary with {'name': {grades}, ...} 
    students_saved = {}

    for student in students:
        students_saved[student] = students[student].grades ## Could have used dictionary comprehension

##  students_saved = {name: student.grades for name, student in students.items()}

    # Overwrites inputted file with new saved data
    with open(filename, 'w') as file:
        json.dump(students_saved, file)

