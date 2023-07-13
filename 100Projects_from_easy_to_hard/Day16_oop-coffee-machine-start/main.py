from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

a = Menu()
b = CoffeeMaker()
c = MoneyMachine()
while True:
    print("Select a choice")
    item = a.get_items()
    print(item)
    order_name = input().lower()
    if order_name == "report":
        b.report()
        c.report()
        continue
    if order_name == "exit":break
    if a.find_drink(order_name):
        if b.is_resource_sufficient(a.find_drink(order_name)):
            if c.make_payment(a.find_drink(order_name).cost):
                b.make_coffee(a.find_drink(order_name))