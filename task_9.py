# Task 9 - Replace First

# Solution 1
def replace_first(items: list):
    if items == []: return items
    else:
        items.append(items[0])
        del items[0]
    return items


print(replace_first([1, 2, 3, 4]))
print(replace_first([]))