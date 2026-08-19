"""
(1) ENCAPSULATION
(2) INHERITANCE <
(3) POLIMORPHISM <
"""
print("===== INHERITANCE =====")
# Parent > Child
#Parent only provides public & protected property(state+method) to children

class Animal:  # parent
    # state
    description = "this class is parent for animals"
    # constructor

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice
    # method

    def make_voice(self):
        print(f"this animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("yes, I can protect!")

    def make_voice(self):
        print(f"this {self.name} can make sound: {self.sound}")


class Cat(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("yes, I can play!")


class Fish(Animal):  # Child

    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("yes, I can swim!")


dog = Dog("Rex", "vov", True)
cat = Cat("Tom", "miyov", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------")
dog.make_voice()
fish.make_voice()
cat.make_voice()

print(Dog.description)
print(f"dog.status: {dog._status}")



print("===== POLIMORPHISM =====")
dog.make_voice()
fish.make_voice()

print("------")
# fish > Fish > Animal >object
a= isinstance(fish, Fish)
b= isinstance( fish, Animal)
c= isinstance( fish, object)
d=isinstance("MIT", object)

result= a and b and c and d
print(f"the result is {result}")

#Fish > Animal > object

data1= issubclass(Fish, Animal)
data2= issubclass(Animal, object)
print("data:", data1, data2)