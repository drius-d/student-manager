# Defining function to load 
import json

def load_students(filename):
    with open(filename, 'r') as file:
        return json.load(file)

