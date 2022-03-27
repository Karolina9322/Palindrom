def is_palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
     return True
    return False
