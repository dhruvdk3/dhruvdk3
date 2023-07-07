print("""
                 
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
print("Welcome to caesar cipher.\nHere you can encode or decode your message.")
alphabet = [
    "a", "b", "c", "d", "e", "f",
    "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x",
    "y", "z"
]


def encrypt(plain_text, shift_amount):
    et = ""
    for i in plain_text:
        x = alphabet.index(i)
        et += alphabet[(x + shift_amount) % len(alphabet)]
    print("\nThe encrypted message is : ", et)


def decrypt(encrypted_text, shift_amount):
    dt = ""
    for i in encrypted_text:
        x = alphabet.index(i)
        dt += alphabet[(x - shift_amount) % len(alphabet)]
    print("\nThe decrypted message is :", dt)


while True:
    direction = input(
        "Select your potion\n1.Encode to encrypt\n2.Decode to decrypt\n3.Quit\n"
    )
    print()
    if direction == "1":
        text = input("Type your message to be encrypted :\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "2":
        text = input("Type your message to be decrypted :\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    elif direction == "3":
        break
    else:
        print("Please enter correct option.")
    print("\n")
