import Logo
from Data import data
import random
import os
random.shuffle(data)
Correct = 0
i = 0
while True and i+1 < len(data):
    print(Logo.logo1)
    
    print(f'Compare A : {data[i]["Name"]}, a {data[i]["Description"]}, from {data[i]["Country"]}')
    print(Logo.logo2)
    print(f'Compare B : {data[i+1]["Name"]}, a {data[i+1]["Description"]}, from {data[i+1]["Country"]}')
    x = input("Who has more followers on Instagram.\nA). A\nB). B\nChoose your option : ").lower()
    if x == "a":
        if data[i]["Followers"] > data[i+1]["Followers"]:
            Correct+=1
            os.system('clear')
            print(f"You are correct.\nCurrent Score : {Correct}")
        else : 
            print(f"That's wrong.\nFinal Score : {Correct}")
            break
    elif x == "b":
        if data[i]["Followers"] < data[i+1]["Followers"]:
            Correct+=1
            os.system('clear')
            print(f"You are correct.\nCurrent Score : {Correct}")
        else : 
            print(f"That's wrong.\nFinal Score : {Correct}")
            break
    i+=1
    if i == len(data):print(f"You guessed all of them correct.\nFinal score : {Correct}")