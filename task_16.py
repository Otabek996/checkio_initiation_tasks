# Task 16 - Is Even

# Solution 1
def is_even(num: int):
    return num % 2 == 0

# Solution 2
is_even = lambda num: num % 2 == 0


print(is_even(2))
print(is_even(5))
print(is_even(0))