def is_palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
     return True
    return False
print("Podaj słowo:")
text = input()

print(is_palindrome(text))
