from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        break

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    chosen_drink = menu.find_drink(user_input)

    if chosen_drink is None:
        print(f"Sorry, repeat your order please.")
        continue

    if user_input in menu.get_items() and coffee_maker.is_resource_sufficient(drink = chosen_drink):
        cost_of_drink = chosen_drink.cost
        is_paid = money_machine.make_payment(cost = cost_of_drink)
        if is_paid:
            coffee_maker.make_coffee(order=chosen_drink)