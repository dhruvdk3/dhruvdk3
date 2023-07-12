Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report_gen():
    for i in resources:
        print(f"{i} : {resources[i]}")

def cost_cheker(cost, price):
    if cost > price:
        x = round(cost - price,2)
        print(f"Here is your change {x}")
        return True
    elif cost == price: 
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False

def cost_eveluation(cost):
    cost += int(input("Please insert a coin.\nhow many quarters? : "))*.25
    cost += int(input("how many dimes? : "))*.10
    cost += int(input("how many nickles? : "))*.05
    cost += int(input("how many pennies? : "))*.01
    return cost

def check_resources(ingrident):
    for i in ingrident:
        if ingrident[i] > resources[i]:
            print(f"​Sorry there is not enough {i}.")
            return False
    return True


def cofee_details(choice):
    return Menu[choice]["ingredients"],Menu[choice]["cost"]


while True:
    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if choice == "report":
        report_gen()
        continue
    if choice == "off":break
    ingrident, price = cofee_details(choice)
    cost = 0
    
    if check_resources(ingrident):
        cost = cost_eveluation(cost)
        if cost_cheker(cost, price):
            for i in ingrident:
                resources[i] = resources[i]-ingrident[i]
            print(f"Here is your {choice} . Enjoy")