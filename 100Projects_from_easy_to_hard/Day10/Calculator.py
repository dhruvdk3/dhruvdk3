print("""
      
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

""")

def calc(a, op, b):
    if op == '/' :
        return a/b
    elif op == '*' :
        return a*b
    elif op == '+' :
        return a+b
    elif op == '-' :
        return a-b
a = float(input("Enter the first number : "))
while True:
    op = input("Select an operation \n+\n-\n*\n/\nPick an operation : ")
    b = float(input("Enter the second number : "))
    try:
        re = calc(a, op, b)
    except :
        print("Please enter a valid expression.")
        continue
    print(f"{a} {op} {b} == {re}")
    a = re
    print("Do you want to continue with this calculation \n1.Yes\n2.Start new calculation\n3.Quit")
    i = int(input())
    if i == 3:break
    if i == 2:a = float(input("Enter the first number : "))