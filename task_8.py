# Task 8 - All Upper I

def is_all_upper(text: str):
    for element in text.split(' '):
        return element.isupper() or element == '' or element.isdigit() or element.isspace()


print(is_all_upper('ALL UPPER'))
print(is_all_upper(''))
print(is_all_upper('444'))
print(is_all_upper('     '))
print(is_all_upper('55 55 5'))
print(is_all_upper('all lower'))