MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 0.00


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${bank:.2f}')


def process_payment():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def process_transaction(coffee_cost):
    payment = process_payment()
    if payment >= coffee_cost:
        change = round(payment - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        global bank
        bank += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


poweredOn = True

while poweredOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        poweredOn = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if process_resources(drink["ingredients"]):
            if process_transaction(drink["cost"]):
                make_coffee(choice, drink["ingredients"])

