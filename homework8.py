def count(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "g":
            count = count + 1
    return count
text = "programming"
result = count(text)
print(result)


def find_voweles(word):
    voweles = 0
    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            voweles = voweles + 1
    return voweles
word = "HelloWorld"
result = find_voweles(word)
print(result)


def asoebis_datvla(text):
    big = 0
    small = 0
    for i in range(len(text)):
        if text[i].isupper():
            big = big + 1
        if text[i].islower():
            small = small + 1
    return big , small
text = "PyThOnIsCoOl"
result = asoebis_datvla(text)
print(result)


def sum_of_digits(text):
    count = 0
    for i in range(len(text)):
        count = count + int(text[i])
    return count
text = "123456789"
result = sum_of_digits(text)
print(result)


def find_max_digit(text):
    big = 0
    for i in range(len(text)):
        if int (text[i]) > big:
            big = int(text[i])
    return big
text = "583921746"
result = find_max_digit(text)
print(result)


def find_a(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "a":
            print(i)
            count = count + 1
    return count
text = "banana"
result = find_a(text)
print(result)


def reserve_(text):
    reverse = ""
    for i in range(len(text) - 1 , -1 , -1):
        reverse = reverse + text[i]
    return reverse
text = "Python"
result = reserve_(text)
print(result)


def palindrome(word):
    reverse = ""
    for i in range(len(word) - 1 , -1 , -1):
        reverse = reverse + word[i]
    return word == reverse
word = "level"
result = palindrome(word)
print(result)


def find_symbols(text):
    letters = 0
    digit = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters = letters + 1
        if text[i].isdigit():
            digit = digit + 1
    return letters , digit
text = "abc123def456gh7"
result = find_symbols(text)
print(result)