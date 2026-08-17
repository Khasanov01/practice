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


print("====== keyword & default arguments =====")
#define
def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"

result3=give_greet(name = "justin", age = 28)
print('result3:', result3)

result4=give_greet("justin")
print('result3:', result4)


print("======= scopes =======")
b=100 #3

def calculate(a, b): #2
    c= a*b #1
    print('c value is', c)

calculate(50, 70)