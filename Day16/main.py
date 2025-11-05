from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    machine_input = input(f"What would you like? ({menu.get_items()}): ").lower()

    if machine_input == "off":
        machine_on = False

    elif machine_input == "report":
        coffe_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(machine_input)

        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
    print()
