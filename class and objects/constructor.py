class Student:
    def __init__(self,fullname):
        print("Adding new student in database")
        self.name=fullname
s1=Student("Vasi")
s2=Student("Basi")
print(s1.name)
print(s2.name)

"""
The following works as well because self is not a keyword-
class Student:
    def __init__(bayleaf,fullname):
        print("Adding new student in database")
        bayleaf.name=fullname
s1=Student("Vasi")
s2=Student("Basi")
print(s1.name)
print(s2.name)
"""