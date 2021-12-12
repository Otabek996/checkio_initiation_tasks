# Task 4 - Number Length

# Solution 1
def number_length(a: int):
    return len(str(a))

# Solution 2
number_length = lambda a: len(str(a))


print(number_length(10))
print(number_length(0))
print(number_length(4))
print(number_length(44))