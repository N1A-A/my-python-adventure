import cowsay
animal = "cat"
if animal == "cow":
    cowsay.cow("Hello Welcome to my project")
elif animal == "cat":
    cowsay.kitty("Hello, have a nice day")
elif animal == "dragon":
    cowsay.dragon("I am a mighty dragon")
else:
    print("This animal is not available")