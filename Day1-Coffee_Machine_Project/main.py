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
    "money": 0,
}

def get_money(amount):
    print(f"Please insert ${amount}")
    quarters_amount = float(input("How many quarters?"))
    dimes_amount =  float(input("How many dimes?"))
    nickles_amount = float(input("How many nickles?"))
    pennies_amount = float(input("How many pennies?"))
    total_coins = (quarters_amount * 0.25) + (dimes_amount * 0.1) + (nickles_amount * 0.05) + (pennies_amount * 0.01)
    amount = round(amount, 2)
    total_coins = round(total_coins, 2)
    if total_coins >= amount:
        resources["money"] += amount
        change = round(total_coins - amount, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def buy_coffee(drink_name, drink):
    has_money = get_money(drink["cost"])
    if has_money:
        for ingredient, amount in drink["ingredients"].items():
            resources[ingredient] -= amount
        print(f"Here is your {drink_name}. Enjoy!")
        return True
    else:
        return False


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(drink):
    for ingredient, amount in drink["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        break
    if user_input == "report":
        report()
        continue
    if user_input in MENU:
        is_there_enough = check_resources(drink = MENU[user_input])
        if is_there_enough:
            buy_coffee(drink_name = user_input, drink = MENU[user_input])
        else:
            continue