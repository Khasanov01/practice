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