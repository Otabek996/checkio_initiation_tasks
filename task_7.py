# Task 7 - Remove All Before

def remove_all_before(items: list, border: int):
    if border not in items or items == []: return items
    while items[0] != border: del items[0]
    return items

        
print(remove_all_before([1, 2, 3, 4, 5], 3))
print(remove_all_before([1, 1, 2, 2, 3, 3], 2))
print(remove_all_before([1, 1, 5, 6, 7], 2))
print(remove_all_before([], 0))