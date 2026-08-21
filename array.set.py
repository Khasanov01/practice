'''ARRAY SET
(1)Arry
(2)Set
(3)Specific operators with set
'''
from array import array
print("=====  Array =====")

numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers1:", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers2:", numbers)

numbers.remove(5)
numbers.pop()
print('number3:', numbers)

del numbers[0:2]
print('number4:', numbers)

print("=====  Set =====")
# Set of unique collection without keeping order!
new_numbers = array("i", [1, 5, 4, 7, 5, 4,  7, 8, 4, 41])
numbs_set = set(new_numbers)

print(f"numbs_set: {numbs_set} and its type: {type(numbs_set)}")

numbs_set.add(200)
print(f"numb_set(2):{numbs_set}")

numbs_set.add(7)
print(f"numb_set(3):{numbs_set}")


print("=====  Specific Set operators: | & - ^  =====")

a={10, 20, 50}
b={20, 40}
result1= a|b #union
result2= a&b #intersection
result3=a-b #difference
result4= a^b #symmetric difference

print("result1", result1)
print("result2", result2)
print("result3", result3)
print("result4", result4)