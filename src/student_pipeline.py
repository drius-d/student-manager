# Building Student class and methods
from exceptions import SubjectAlreadySubmitted, SubjectNotSubmitted

class Student():
    def __init__(self, name, grades):
        self._name = name
        self._grades = grades

    # _name should be read only outside of class methods
    @property
    def name(self):
        return self._name

    # _grades should be read only outside of class methods
    @property
    def grades(self):
        return self._grades

    # method to add grade to student
    def add_grade(self, subject, grade):
        if subject in self._grades:
            raise SubjectAlreadySubmitted(subject)
        else:
            self._grades[subject] = grade

    # method to change grade 
    def change_grade(self, subject, grade):
        if subject not in self._grades:
            raise SubjectNotSubmitted(subject)
        else: 
            self._grades[subject] = grade

    # method to calculate student's average
    def calculate_average(self):
        if not self._grades:
            return 0
        else:
            return sum(self._grades.values()) / len(self._grades.values())



    




    

    




