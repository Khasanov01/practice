"""
Tuple
(1) What is tuple: tuple vs list
(2) Unpacking arguments
(3) zip
"""

print("===== What is tuple: tuple vs list =====")
# Java/PHP/NodeJS array => Python list

# literal
numbs = [3, 5, 1, 2]

# constructor
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"

#try to avoid these
people="Andrew", "John"
animals="dog",

print("===== Unpacking Arguments =====")

groups=("MIT", "Flexy", "Devex", "MG")
(x, y, *z)= groups
print(f"the x:{x} and y:{y}")
print(f"the value of z is:{z}") #list

# *args > Tuple

def calculate(*args):
    print("args:", args)
    total=1
    for x in args:
        total*=x
    print(f"the type(args) value:{type(args)}")
    print(f"the  value: {total}")
    return total

#call
calculate(1, 7, 2, 3)
print("-----")
calculate(0, 2, 300)
print("-----")
calculate(5, 7)




print("-----")
#**kwargs > dictionary
def introduce(**kwargs):
    print(f"the type(kwargs) value:{type(kwargs)}")
    print(f"Hi, I'm {kwargs["name"]} and I'm {kwargs["age"]} years old")
    pass

#call
introduce(name="justin", age=25)
introduce(name="Shawn", age=35, single= True)