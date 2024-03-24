class Student:
    def __init__(self, name, age, perc):
        self.name = name
        self.age = age
        self.perc = float(perc)

    def details(self):
        print("<== Student Details ==>".center(40))
        return f'''Student name : {self.name}
Student age : {self.age}
Student percentage : {self.perc}
Student grade : '''

    def calc_grade(self):
        if self.perc > 100:
            return "Nope, Seriously \U0001F923 \U0001F606 \U0001F923"
        elif self.perc > 90:
            return "O"
        elif self.perc > 80:
            return "A"
        elif self.perc > 70:
            return "B"
        elif self.perc > 60:
            return "C"
        elif self.perc > 50:
            return "D"
        elif self.perc > 40:
            return "E"
        else:
            return "F"
    
name = input("Enter name of student : ")
age = input("Enter age of student : ")
percentage = input("Enter percentage of student : ")
s1 = Student(name, age, percentage)
print(s1.details(),s1.calc_grade())