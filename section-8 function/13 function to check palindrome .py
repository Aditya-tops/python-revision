def check_palindrome(word):
    l = len(word)
    for i in range(l // 2):  # Added colon
        if word[i] != word[l - i - 1]:
            return False
    return True

print(check_palindrome("racecar"))  # This will print True
print(check_palindrome("hello"))    # This will print False
