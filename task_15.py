# Task 15 - Correct Sentence

def correct_sentence(text: str):
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


print(correct_sentence("Greetings, friends"))
print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends."))