# Building Student class and methods

class Student():
    def __init__(self, name, grades = dict):
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
    def add_grade(self, subject, grade, _grades):
        self._grades

    # method to change grade 
    def change_grade(self, subject, grade, _grades):
        pass

    # method to calculate student's average
    def calculate_average(self, _grades):
        pass

    

    




