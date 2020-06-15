class Person:
    def __init__(self,name):
         self.name=name
    def designation(self):
        raise NotImplementedError("subclass must implemented abstract method")
class Employee(Person):
    def designation(self):
        return "software engineer"
class Doctor(Person):
    def designation(self):
        return "cardiologost"
class Student(Person):
    def designation(self):
        return "graduate enginer"
persons=[Employee('guido Van Rossum'),Doctor('chalapthi'),Student('robert')]
for person in persons:
    print(person.name + " : "+ person.designation())
