'''
Functions
(1) define vs call
(2) parameter vs argument
(3) keyword  vs default arguments
(4) scope
'''

print("===== define {parameter} and call{argument} =====")
# buitl in function> print() type ()
# functions - reusable block of code
# instead of {} in JAVA, python uses indentation!

# define - parameter


def greet(a):
    print(f"how do you do:{a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# call - argument

result1 = greet("men")
print(result1)

result2 = greeting("justin")
print(result2)