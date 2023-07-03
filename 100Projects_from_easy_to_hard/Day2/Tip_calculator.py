bill = int(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
no_of_persons = int(input("How many people to split the bill?"))
amount = (bill+(bill*tip/100))/no_of_persons
final_amount = round(amount,2)
print(f"Each person should pay: {final_amount}")