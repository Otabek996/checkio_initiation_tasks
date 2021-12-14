# Task 13 - Nearest Value

def nearest_value(values: set, one: int):
    values = list(values)
    answers = []
    for num in values:
        if num == 0:
            num += 1
            answers.append(abs(one - num))
        else: answers.append(abs(one - num))
    return values[answers.index(min(answers))]
    

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
print(nearest_value({4, 8, 10, 11, 12, 17}, 9))
print(nearest_value({-1, 2, 3}, 0))
print(nearest_value({0, -2}, -1))