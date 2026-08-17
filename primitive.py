print("========= number ==========")
# in JAVA, variable is a name of a storage location
# in Python, variable is a named reference

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count:{count} and the type:{count_type}")
print("=============")
result1 = count.bit_count() #method
result2 = count.numerator #state
print(result1, result2)

print("========= tsring ========")
#methods: upper(), lower(), title(), find(), replace()
course = "AI python Fullstack"
result = type(course)
print(f"type of course(1): {result}")

result=course.title()
print(f"result(2):{result}")

result=course.upper()
print(f"the result(3):{result}")

result=course.replace("AI", "artificial intelligance")
print(f"the result(4):{result}")
print(course)

print("========= boolean ========")
#Functions> type() input() bool() int() str()
y = input("give your input for y:")
print(f"y is: {y}")

result=y.isnumeric()
print(f"input is {result}")

#truthy and falsy values
#truthy: true, 100, -100, "abc"
#falsy: false, 0, "", none
test_falsy="" or False or None or 0
print("the test_falsy", bool(test_falsy))

test_truthy="abc" or True or 100
print("the test_truthy", bool(test_truthy))