# Task 5 - End Zeros

# Solution 1
def end_zeros(num: int):
    acc = 0
    for number in str(num)[::-1]:
        if number != '0': return acc
        else: acc += 1
    return acc


print(end_zeros(0))
print(end_zeros(1))
print(end_zeros(10))
print(end_zeros(101))
print(end_zeros(245))
print(end_zeros(100100))