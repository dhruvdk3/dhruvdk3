# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                     'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                     'Y', 'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

l = int(input("Welcome to the PyPassword Generator!\nHow many letters would you like in your password?\n"))
s = int(input("How many symbols would you like?\n"))
n = int(input("How many numbers would you like?\n"))
x = l-s-n
p = []
for i in range(0,x):
    a = random.randint(0, len(CHARACTERS)-1)
    p.append(CHARACTERS[a])
for i in range(0,s):
    a = random.randint(0, len(SYMBOLS)-1)
    p.append(SYMBOLS[a])
for i in range(0,n):
    a = random.randint(0, len(DIGITS)-1)
    p.append(DIGITS[a])
print(p)
cp = p
print(cp)
fp = []
for i in range(0,len(p)):
    a = random.randint(0,len(cp)-1)
    fp.append(cp.pop(a))
finalpassword = ""
for i in fp:
    finalpassword +=i
print(finalpassword)

