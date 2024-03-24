class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Lion(Animal):
    def __str__(self):
        return f'''<== Animal Species : {self.species} ==>
Name : {self.name}
Age : {self.age}'''
    
class Elephant(Animal):
    def __str__(self):
        return f'''<== Animal Species : {self.species} ==>
Name : {self.name}
Age : {self.age}'''
    
class Giraffe(Animal):
    def __str__(self):
        return f'''<== Animal Species : {self.species} ==>
Name : {self.name}
Age : {self.age}'''

a1 = Lion("Simba","Lion",20)
a2 = Elephant("Gajraj","Elephant",35)
a3 = Giraffe("Lambu","Giraffe",15)

print(a1,a2,a3,sep="\n")