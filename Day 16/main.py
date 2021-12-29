from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

powered_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while powered_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        powered_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)