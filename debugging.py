'''PACKAGES & DEBUGGING
(1) Python packages & Core package
(2) Package Manager & External Package
(3) Debugging
'''
from PIL import Image
import turtle
print("===== Python Packages & Core Package =====")
""" Python Packages/Modules: Core, File and External """
# Core Packages https://docs.python.org/3/library


# Core package
 t = turtle.Turtle()
 t.shape("turtle")
 t.speed(2)
t.circle(150)

turtle.done()

print("------")
my_file = open('material/message.txt', 'r')
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with
with open('material/message.txt', 'r') as your_file:
    your_content = your_file.read()
    print('message:', your_content)
print("done")


print("===== Package Manager & External Package =====")
""" Package Managers: pip pipenv npm yarn composer brew """
# External Package > https://pypi.org/

with Image.open("material/sign-up-form.png") as img_obj:
   resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")


print("===== Debugging =====")
def get_summary(*args):  # DEFINE
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # find the bug via debugging

test=100
result = get_summary(1, 2, 3, 4, 5)  # CALL
print("result:", result)
