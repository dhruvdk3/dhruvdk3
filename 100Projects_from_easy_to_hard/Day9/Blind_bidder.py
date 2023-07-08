import os
print("""
      
                         ___________
                         \         /
                          )_______(
                          |\"\"\"\"\"\"\"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )\"\"\"\"\"\"\"(
                         /_________\\
                       .-------------.
                      /_______________\\
""")

print("Welcome to blind bid : ")

bid = {}
i = 1
while True:
    name = input("What is your name? : ")
    price = int(input("What is your bid? : $"))
    bid[name] = price
    x = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if x == "yes":
        os.system('clear')
    elif x == "no":
        break
max = 0
name = ""
for i in bid:
    if bid[i] > max :
        name = i
        max = bid[i]
print(f"The winner is {name} with a bid of ${max}")