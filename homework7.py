#3
text = "PyThOnIsCoOl"
big = 0
small = 0
for N in range(len(text)):
    if text[N].isupper():
        big = big + 1
    elif text[N].islower():
        small = small + 1
print(big)
print(small)

#8
word = "reser"
reverse = "" 
for N in range(len(word) -1 , 0 - 1 , -1):
    reverse = reverse + word[N]
if word == reverse:
    print(True)
else:
    print(False)

#9
text = "abc123def456gh8"
letters = 0
digits = 0
for N in range(len(text)):
    if text[N].isalpha():
        letters = letters + 1
    elif text[N].isdigit():
        digits = digits + 1
print("letters:" , letters)
print("digit" , digits)