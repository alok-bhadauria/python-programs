class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def details(self):
        return f'''Student name : {self.name}
Student age : {self.age}
Student grade : {self.grade}'''
    
name = input("Enter name of student : ")
age = input("Enter age of student : ")
grade = input("Etner grade of student : ")
s1 = Student(name, age, grade)
print(s1.details())