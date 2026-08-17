print("======= iterable objects & RANGE =======")
# iterable objects> string dict tuple list range map filter
range_obj = range(3)
print("rabge_object:", range_obj)

text = "MIT"
for letter in text:
    print(f"the letter:{letter}")


for ele in range_obj:
    print("the range object", ele)


print("======= DICTIONARY =======")
# Dictionary is json object
person = {"name": "justin", "age": 25, "single": True}  # 1st way

person_obj = dict(name="justin", age=25, single=True)  # 2nd way

print(person)
print(person_obj)

name = person_obj["name"]
print('name:', name)



#method get()
name=person_obj.get("name")
print(name)
hobby=person_obj.get("hobby")
balance=person_obj.get("balance", 0)
print(f"the name:{name} and the hobby:{hobby} and the balance:{balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key:{key} and value=>{person_obj.get(key)}")