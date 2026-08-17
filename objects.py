''' OBJECTS
(1) what is an object
(2) iterable objects & range
(3) DICTIONARY
(4) error handling system
'''

import array  # package or module
import math  # package
from math import ceil, asin

print("====== what is an object ======")
# an object has state and method properties
# everything is object in python
print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm> OOP functional & Proggramming
# OOP 4 concepts> Abstruction Encapsulation Inheritance polimorphism
result1 = math.ceil(97.7)  # CALL
print(result1)

result2 = ceil(98.7)
print(result2)


print("========= error handling system =========")
car_dict = dict(name="Toyota", year=2006, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print(result)
except KeyError as err:
    print('no origin state property found:', err)
except AttributeError as err:
    print('no speed found:', err)
else:
    print("Logic executed successfully without errors")
finally:
    print("final closing logic")
