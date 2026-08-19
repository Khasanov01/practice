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

animals.clear()
print('clear animals:', animals)

exist2 = animals.index("cat")
print("cat exist2:", exist2)
