'''Class
(1)what is class
(2)ordinary vs static properties
(3)special methods
'''
print("======== what is a class ========")
# class=> blueprint for an object creation
# structure> state constructor method


class Person():
    # state
    message = "static state property"
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method

    def introduce(self):
        print(f"Hi, Im {self.name}")

    def say_age(self):
        print(f"Im {self.age} years old")
    
    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("justin", 25)
person2 = Person("martin", 35)

# ordinary state
name = person1.name
print(name)

# ordinary method
person1.introduce()
person2.say_age()

print("======== ordinary vs static properties ========")
# static state
new_message = Person.message
print(new_message)

# static method
Person.explain()
