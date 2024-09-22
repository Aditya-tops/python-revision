word = "madam"

l = len(word)

# looping through the first half of the word
palindrome_flag = True
for i in range(l // 2):
        # print(word[i])
    # print(word[l-i-1])
    if word[i] != word[l - i - 1]:
        palindrome_flag = False
        break

if palindrome_flag:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
