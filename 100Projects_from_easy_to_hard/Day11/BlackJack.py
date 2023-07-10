import random
import os

while True:
    start = int(input("Do you want to play a game of Blackjack?\n1.Yes\n2.No\n"))
    if start == 2:
        exit()
    os.system("clear")
    print(
        """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           

        """
    )
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    if user_sum == 22:
        a = user_cards.index(11)
        user_cards[a] = 1
        user_sum = sum(user_cards)
    x = True
    while True:
        print()
        print(f"Your cards: {user_cards}\nYour current score : {user_sum}\n")
        print(f"Computer's first card : {computer_cards[0]}")
        print()
        choice = int(input("Do you want to draw another card\n1.Yes\n2.No\n"))
        print()
        if choice == 2:
            print(f"Your cards: {user_cards}\nYour final score : {user_sum}\n")
            break
        else:
            user_cards.append(random.choice(cards))
            user_sum = sum(user_cards)
            if user_sum > 21:
                if 11 in user_cards:
                    a = user_cards.index(11)
                    user_cards[a] = 1
                    user_sum = sum(user_cards)
                else:
                    print(f"Your cards: {user_cards}\nYour final score : {user_sum}\n")
                    print(
                        f"Computer's final hand : {computer_cards}\nComputer's final score : {computer_sum}\n"
                    )
                    print("You went over.\nYou lost\n")
                    x = False
                    break

    while x:
        if computer_sum > user_sum and computer_sum < 22:
            print(
                f"Computer's final hand : {computer_cards}\nComputer's final score : {computer_sum}\n"
            )
            print("You lost\n")
            break
        elif computer_sum == user_sum:
            print(
                f"Computer's final hand : {computer_cards}\nComputer's final score : {computer_sum}\n"
            )
            print("Its a draw.")
            break
        elif computer_sum > 21:
            if 11 in computer_cards:
                a = computer_cards.index(11)
                computer_cards[a] = 1
                computer_sum = sum(computer_cards)
            else:
                print(
                    f"Computer's final hand : {computer_cards}\nComputer's final score : {computer_sum}\n"
                )
                print("You win\n")
                break
        elif user_sum > computer_sum:
            if computer_sum <= 16:
                computer_cards.append(random.choice(cards))
                computer_sum = sum(computer_cards)
            else:
                print(
                    f"Computer's final hand : {computer_cards}\nComputer's final score : {computer_sum}\n"
                )
                print("You won\n")
                break
