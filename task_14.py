# Task 14 - Between Markers (simplified)

def between_markers(text: str, begin: str, end: str):
    return text[(text.index(begin) + 1):(text.index(end))]


print(between_markers('What is >apple<', '>', '<'))