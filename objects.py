''' OBJECTS
(1) what is an object
(2) iterable objects & range
(3) DICTIONARY
(4) error handling system
'''

import array #package or module
import math #package
from math import ceil, asin

print("====== what is an object ======")
#an object has state and method properties
#everything is object in python
print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

#Paradigm> OOP functional & Proggramming
#OOP 4 concepts> Abstruction Encapsulation Inheritance polimorphism 
result1 = math.ceil(97.7) #CALL
print(result1)

result2=ceil(98.7)
print(result2)
