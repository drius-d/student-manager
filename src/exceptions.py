class SubjectAlreadySubmitted(Exception):
    def __init__(self, subject):
        super().__init__(f"Error: grade for {subject} already exists.")

class SubjectNotSubmitted(Exception):
    def __init__(self, subject):
        super().__init__(f"Error: {subject} does not exist.")

class NotAlpha(Exception):
    def __init__(self, string):
        super().__init__(f"Error: {string} is not contains non-alphabetic characters")