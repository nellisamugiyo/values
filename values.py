#using oop to record the average grade of students in a school
# making life easier


class Student (object):
    
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades
    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        print("The average for student "+ self.name+" is "+str(average))
mercy=Student(19,"mercy","female",[99,98])
Stanely=Student(18,"Stanely","male",[100,89])     
philani = Student(20,"Philani Sithole","Male",[64,65])
sarah = Student(19,"Sarah Jones","Female", [82,58])
sarah.compute_average()
mercy.compute_average()
Stanely.compute_average()
philani.compute_average()