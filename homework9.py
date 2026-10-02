city = "Tbilisi"
def show():
    print(city)
show()    
#დაიბეჭდება "Tbilisi" , რადგან city არის გარეთა სკოუპში.
#print(city) კითხულობა რა წერია city-ში და ბეჭდავს Tbilisi-ს

#def make():
    #fruit = "aplle"
#make()
#print(fruit)
#fruit შეიქმნა ფუნქციის შიგნით,print(fruit) ამიტომ გარედან ვერ კითხულობს მის მნიშვნელობას და არაფერი დაიბეჭდება.



x = 10
def change():
    x = 99
    print("shignit:" , x)
change()
print("garet:" , x)
#ფუნქციის შიგნით შექმნილი x არის ცალკე ცვლადი , ამიტომ print("shignit:" , x) ბეჭდავს 99-ს, ხოლო გარეთ არსებული x 10-ს


def double(n):
    n = n * 2
    return n
n = 5
result = double(n)
print(n , result)
#n პარამეტრი ფუნქციის სკოუპშია, ამიტომ ფუნქციის შიგნით შეცვლილი n გარეთ არსებულ n-s არ ცვლის , დაბეჭდავს 5-ა და 10-ს.

def check(age):
    if age >= 18:
        status = "zrdasruli"
    else:
        status = "bavshvi"
    print(status)
check(20)
check(7)
#status იქმნება if-ის სკოუპში, მაგრამ if-ს ცალკე სკოუპი არ აქვს, ამიტომ print(status) ფუნქციის შიგით კითხუობს მის მნიშვნელობას.

def last_letter(text):
    for letter in text:
        pass
    return letter
print(last_letter("python"))
#letter იქნება for ციკლში, მაგრამ for-ს ცალკე სკოუპი არ აქვს, ბოლო მნიშვნელობას იღებს n-ს, ფუნქცია მას აბრუნებს და იბეჭდბა n.

def scope_1():
    secret = 42
    return secret
def scope_2(secret):
    print(secret)
x = scope_1()
scope_2(x)
#გამოვა შეცდომა რადგან secret არის scope_1- ის სკოუპში და scope_2 მას ვერ ხედავს.
#სწორ კოდში: scope_1 აბრუნებს 42-ს, შემდეგ გადაეცემა scope_2-ს და დაიბეჭდება 42.


def count_a(text):
    count = 0
    for ch in text:
        if ch == "a":
            count = count + 1
    return count
count = count_a("banana")
print(count)
#ფუნქცია "banana"-ში a ითვლება, და return-ით აბრუნებს რაოდენობას. დაიბეჭდება 3