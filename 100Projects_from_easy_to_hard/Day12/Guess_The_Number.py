import random
print("""
   _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\\\___ \     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\\
                                                                                                      
                                                                                                      
    """)
print("Welcome to guessing number game.")
x = random.randint(1,100)
print("The number is between 1 and 100")
print("Choose a dificulty")
dificulty = int(input("1.Easy(10 attempts)\n2.Normal(7 attempts)\n3.Hard(5 attempts)\nEnter your choice : "))
attempts = 0
if dificulty == 1:
    attempts = 10
elif dificulty == 2:
    attempts = 7
else :
    attempts = 5
while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Choose a number : "))
    if guess > x:
        print("Too High.\nGuess Again.\n")
        attempts-=1
    elif guess < x:
        print("Too Low.\nGuess Again.\n")
        attempts-=1
    elif guess == x :
        print(f"You guessed it correct. The answer was {x}")
        break
    if attempts == 0:
        print("You've run out of guesses, you lose.")