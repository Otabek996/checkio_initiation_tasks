# Task 12 - Beginning Zeros

# Solution 1
def beginning_zeros(number: str):
    acc = 0
    for i in number:
        if i == '0': acc += 1
        else: return acc
    return acc


print(beginning_zeros('100'))
print(beginning_zeros('010'))
print(beginning_zeros('001'))
print(beginning_zeros('0000'))