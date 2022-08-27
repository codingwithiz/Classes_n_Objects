class student:
'''
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created
'''
    def __init__(self , name , major , gpa , is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

