
def is_palindrome(s):
    # Check if the length of the string is 0 or 1
    if len(s) < 2:
        return True

    # Compare the first and last characters
    if s[0] != s[-1]:
        return False

    # Recursively check the rest of the string
    return is_palindrome(s[1:-1])

print(is_palindrome("ianai")) # True

print(is_palindrome("amo")) # False

print(is_palindrome("ipi")) # True

print(is_palindrome("op po")) # True