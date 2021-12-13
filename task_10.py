# Task 10 - Max Digit

# Solution 1
def max_digit(number: int):
    numbers = []
    for num in str(number):
        numbers.append(int(num))
    return max(numbers)


print(max_digit(0))
print(max_digit(52))
print(max_digit(634))
print(max_digit(1000))