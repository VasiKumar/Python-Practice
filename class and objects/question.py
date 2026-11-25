"""
Create student class that takes name & marks 
of 3 subjects as arguments in constructor. Then 
create a method to print the average. 
"""

class Student:
    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def printing(self):
        marks=sum(self.marks)/len(self.marks)
        print(self.name,"'s Average score is: ",marks)

s1=Student("Basi", [99,98,97])    
s1.printing()
s1.name="Kk"
s1.printing()