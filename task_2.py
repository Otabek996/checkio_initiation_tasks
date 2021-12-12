# Task 2 - First Word (simplified)

# Solution 1
def first_word(text: str):
    return text.split(' ')[0]

# Solution 2
first_word = lambda text: text.split(' ')[0]

print(first_word("Hello world"))
print(first_word("a word"))
print(first_word("hi"))