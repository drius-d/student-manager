from group_functionality import display_screen
from student_loader_saver import load_students
from student_pipeline import Student

def main():
    

    # loading students from JSON file
    student_data = load_students('students.json')

    # creating dictionary. keys are names of student. values are Student class objects.
    students = {}

    for name, grades in student_data.items():
        student = Student(name, grades)

        students[name] = student

    display_screen(students)

        
if __name__ == "__main__":
    main()
