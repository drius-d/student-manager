
def main():
    from student_manager import load_students
    from student import Student

    student_data = load_students('students.json')

    students = {}

    for name, grades in student_data.items():
        student = Student(name, grades)

        students[name] = student

    print(students)
        

if __name__ == "__main__":
    main()
