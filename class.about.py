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


print("======== special/magic methods ========")
#pythons most common special methods are below:
#__init__< __new__< __str__< __call__, __len__

class Car():
    #state
    description="this class makes cars"
    #constructor
    def __new__(cls, *args):
        print("__new__ is executed")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name=name
        self.year=year
    #method
    def start_engine(self):
        print(f"The {self.name} started engine!")

    def stop_engine(self):
        print(f"The {self.name} stopped engine!")
    def __str__(self):
        return f"{self.name} is made in {self.year}"
    def __call__(self):
        print("object called as function")
        return True


my_car= Car('Ferrari', 2025)
my_car.start_engine()
my_car.stop_engine()

print("--------")
your_car=Car("Toyota", 2026)
print(your_car)


response =your_car() #look like function
print(response)