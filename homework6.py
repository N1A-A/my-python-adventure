#1
text = "programming"
count = 0
for letter in text:
    if letter == "g":
        count = count + 1
print(count)

#2
text = "HelloWorld"
count = 0
for litter in text:
    if letter == "a" or letter =="o" or letter == "i" or letter == "o" or letter == "u":
        count = count + 1
print(count)

#3
text = "PyThOnIsCoOl"
big_count = 0
small_count = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "A" or text[i] == "B" or text[i] == "C" or text[i] == "D" or text[i] == "E" or text[i] == "F" or text[i] == "G" or text[i] == "H" or text[i] == "I" or text[i] == "J" or text[i] == "K" or text[i] == "L" or text[i] == "M" or text[i] == "N" or text[i] == "O" or text[i] == "P" or text[i] == "Q" or text[i] == "R" or text[i] == "S" or text[i] == "T" or  text[i] == "U" or text[i] == "V" or text[i] == "W" or text[i] == "X" or text[i] == "Y" or text[i] == "Z":
        big_count = big_count + 1
    else:
        small_count = small_count + 1
print(big_count)
print(small_count)

#4
text = "123456789"
sum = 0
for i in range(len(text)):
    sum = sum + int(text[i])
print(sum)

#5
text = "583921746"
big = 0
for i in range(len(text)):
    if int(text[i]) > big:
        big = int(text[i])
print(big)

#6
text = "banana"
for i in range(len(text)):
    if text[i] == "a":
        print(i)

#7
text = "Python"
reverse = ""
for i in range(len(text) -1, -1, -1):
    reverse = reverse + text[i]
print(reverse)

#8
word = "level"
palindrome = True


#9
text = "abc123def456gh7"
letters = 0
digits = 0
for i in range(len(text)):
    if text[i] >= "0" and text[i] <= "9":
        digits = digits + 1
    else:
        letters = letters + 1
print("Letters:" , letters)
print("Digital:" , digits)

#10
password = "GAmb123!"
lengh = False
digit = False
yes_letter = False
no_letter = False
for i in range(len(password)):
    if password[i] >= "0" and password[i] <= "9":
        digit = True
    if password[i] >= "A" and password[i] <= "Z":
        yes_letter = True
    if password[i] >= "a" and password[i] <= "z":
        no_letter = True
if len(password) >= 8:
    lengh = True
if lengh == True and digit == True and yes_letter == True and no_letter == True:
    print("Strong password")
else:
    print("Weak password")

#
text = "აი, რა მზის სიზმარია"
new_text = ""