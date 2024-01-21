class Employee:
    company = 'BigCorp'
    def __init__(self, name, age):
        self.name =  name
        self.age = age
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Dog:
    pass 

fried = Employee('fried', 12)
