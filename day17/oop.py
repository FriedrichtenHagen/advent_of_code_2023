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
    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Engineer(Employee):
    salary = 10000

class Dog:
    pass 

fried = Employee('fried', 12)
print(fried)

test = Engineer('fred', 55)
print(test.salary)