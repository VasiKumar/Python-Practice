class Student:
    def __init__(self,fullname):
        print("Adding new student in database")
        self.name=fullname
s1=Student("Vasi")
print(s1.name)