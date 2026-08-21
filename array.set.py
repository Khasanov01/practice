'''ARRAY SET
(1)Arry
(2)Set
(3)Specific operators with set
'''
print("=====  Array =====")
from array import array

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


