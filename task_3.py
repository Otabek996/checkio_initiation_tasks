# Task 3 - Acceptable Password I

# Solution 1
def is_acceptable_password(password: str):
    return len(password) > 6

# Solution 2
is_acceptable_password = lambda password: len(password) > 6


print(is_acceptable_password('short'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))