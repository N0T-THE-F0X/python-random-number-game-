import random
print(r"    _        _      _   _   ")
print(r"   //\      | |     \ \/ /  ")
print(r"  //_\\     | |      \/ /   ")
print(r" //___\\    | |__    / / \  ")
print(r"//     \\   |____|  /_/ \_\ ")
print()
print("Random number game")

while True:
    print()
    x = input("pick a random number 0-10: ")
    y = random.randint(0,10)

    if int(x) == y :
        print("corect it was:", y)

    else: 
        print("Sorry better luck next time!")