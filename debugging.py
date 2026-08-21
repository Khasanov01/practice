'''PACKAGES & DEBUGGING
(1) Python packages & Core package
(2) Package Manager & External Package
(3) Debugging
'''
import turtle
print("===== Python Packages & Core Package =====")
""" Python Packages/Modules: Core, File and External """
# Core Packages https://docs.python.org/3/library


# Core package
#t = turtle.Turtle()
#t.shape("turtle")
#t.speed(2)
#t.circle(150)

#turtle.done()

print("------")
my_file=open('material/message.txt', 'r')
try:
    content=my_file.read()
    print("content:", content)
finally:
    my_file.close()

#with
with open('material/message.txt', 'r') as your_file:
    your_content=your_file.read()
    print('message:', your_content)
print("done")
