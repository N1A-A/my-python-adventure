city = "Tbilisi"
def show():
    print(city)
show()    


#def make():
    #fruit = "aplle"
#make()
#print(fruit)



x = 10
def change():
    x = 99
    print("shignit:" , x)
change()
print("garet:" , x)


def double(n):
    n = n * 2
    return n
n = 5
result = double(n)
print(n , result)

def check(age):
    if age >= 18:
        status = "zrdasruli"
    else:
        status = "bavshvi"
    print(status)
check(20)
check(7)


def last_letter(text):
    for letter in text:
        pass
    return letter
print(last_letter("python"))


def scope_1():
    secret = 42
    return secret
def scope_2(secret):
    print(secret)
x = scope_1()
scope_2(x)


def count_a(text):
    count = 0
    for ch in text:
        if ch == "a":
            count = count + 1
    return count
count = count_a("banana")
print(count)
