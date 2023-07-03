import random
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
x = random.randint(0,2)
l = ["    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n\n","    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)\n\n","    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)\n\n"]
if a == 0:
    print(l[a])
    if x == 0:
        print("Computer chose:\n")
        print(l[x])
        print("It's a draw")
    elif x == 1:
        print("Computer chose:\n")
        print(l[x])
        print("You lose")
    else : 
        print("Computer chose:\n")
        print(l[x])
        print("You win!")
elif a== 1:
    print(l[a])
    if x == 0:
        print("Computer chose:\n")
        print(l[x])
        print("You win!")
    elif x == 1:
        print("Computer chose:\n")
        print(l[x])
        print("It's a draw")
    else : 
        print("Computer chose:\n")
        print(l[x])
        print("You lose")
else:
    print(l[a])
    if x == 0:
        print("Computer chose:\n")
        print(l[x])
        print("You lose")
    elif x == 1:
        print("Computer chose:\n")
        print(l[x])
        print("You win!")
    else : 
        print("Computer chose:\n")
        print(l[x])
        print("It's a draw")


