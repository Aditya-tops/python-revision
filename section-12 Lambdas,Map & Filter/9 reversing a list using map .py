'''
word = "abcdefghijklmno"
print(word[3:8:2])
# [start:end:step]
print(word[3:8:3])
print(word[::2])
print(word[::1])
print(word[::-1])
'''
words = ["Python","Java","Javascript","C++"]
reversed_words = list(map(lambda word:word[::-1],words))
print(reversed_words)

