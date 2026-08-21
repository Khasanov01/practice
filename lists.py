"""
List
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumerate, map and filter
"""

print("===== Working with lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello World!")
print(f"the result: {result} and size: {len(result)}")


print("-------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("===== List methods =====")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]
letters.append("c")  # add from behind

print("the append results:", letters)

letters.insert(0, "z")  # add in front
print("the insert result:", letters)

size = len(letters)-1
result1 = letters.pop(size)  # pop from behind
print(f"the pop result:{result1} and letters:{letters}")

result2 = letters.pop(0)  # pop in front
print(f"the pop in front result:{result2} and letters:{letters}")


print("--------")
animals = ["cat", "dog", "capybara", "fish", "lion"]
print("animal:",  animals)

animals.remove("lion")
print("remove:", animals)

del animals[2:4]
print("delete:", animals)


exist = animals.index("cat")
print("cat exist:", exist)

# animals.clear()
# print('clear animals:', animals)

if "cat" in animals:
    print("cat index", animals.index("cat"))
else:
    print("cat doesn't exist")

print("----------")
numbers = [2, 20, 12, 8, 57]

numbers.sort()
print("sort default:", numbers)

numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable> sort function index()
nums = [2, 20, 12, 100]
new_nums = sorted(nums)
print(f"immutable sorted func:{new_nums} and the old list: {nums} ")


print("===== Lambda Functions =====")
# lambda functionns are small anonymous functions


def calculate(x, y): return x*y


result = calculate(3, 5)
print('the result is', result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)


print("====== enumerate, map and filter ======")
# enumerate for index&value

animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("elements:", element)

print("-------")

for (index, value) in enumerate(animals):
    print(f"the index:{index} and value is {value}")

# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)  # dict
result = car_obj.items()
for (key, value) in result:
    print(f"the key:{key} and value is {value}")

print("-------")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_cars(1):", new_cars)


result1 = map(lambda car: car[0], cars)
print(' and its type', result1, type(result1))

new_cars = list(result1)
print(f"new_cars(2): {new_cars}")


print("-------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(
    f"the result_filter: {result_filter} and its type: {type(result_filter)}")
print(list(result_filter))
