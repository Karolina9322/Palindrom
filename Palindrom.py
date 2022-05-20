def is_palindrome(text):

    """Funkcja sprawdzająca czy dany wyraz/zdanie jest palindromem.
     Funkcja usuwa ze sprawdzanego tekstu znaki interpunkcyjne i spacje."""

    signs = [",",".",":",";","!","?"," ","-","..."]
    for i in signs: 
        text = ("".join(text.split()))
        text = text.lower().replace(i, "")
        if text == text[::-1]:
            return True
        return False

# kilka testów:
print(is_palindrome("Wakacje"))
print(is_palindrome("KajaK"))
print(is_palindrome("Popija rum As, Samuraj i Pop"))
print(is_palindrome("Marzena pokazała Zakopane z ram"))
print(is_palindrome("Kobyła ma mały Bok"))
print(is_palindrome("Wół utył i ma miły tułów"))

print()

text = (input("Podaj własne słowo/zdanie: "))
print(is_palindrome(text))
