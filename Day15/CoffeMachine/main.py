from data import MENU
from data import resources

def show_report():
    """Print the current remaining resources"""
    for resource in resources:
        if resource == "water" or resource == "milk":
            resource_value = f"{resources[resource]}ml"
        elif resource == "coffee":
            resource_value = f"{resources[resource]}g"
        else:
            resource_value = f"${resources[resource]}"

        print(f"{resource.capitalize()}: {resource_value}")

def format_ingredients_list(ingredients):
    """Receives a list of insufficient ingredients and returns the formatted text"""
    if len(ingredients) == 1:
        return ingredients[0]
    elif len(ingredients) == 2:
        return f"{ingredients[0]} and {ingredients[1]}"
    else:
        return f"{ingredients[0]}, {ingredients[1]} and {ingredients[2]}"

def enough_resource(coffee_type):
    """Return True if there is enough resources for the coffee, return False otherwise"""
    coffee_type_ingredients = MENU[coffee_type]["ingredients"]
    insufficient_ingredients = []

    for ingredient in coffee_type_ingredients:
        resource_needed = coffee_type_ingredients[ingredient]
        resource_avaible = resources[ingredient]

        if resource_avaible < resource_needed:
            insufficient_ingredients.append(ingredient)

    if insufficient_ingredients:
        ingredients_text = format_ingredients_list(insufficient_ingredients)
        print(f"Sorry there is not enough {ingredients_text}.")
        return False        

    return True
        
def make_coffee(coffee_type):
    """Deduct resources and print the chosen coffee"""
    for ingredient in MENU[coffee_type]["ingredients"]:
        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]

    print(f"Here is your {coffee_type} ☕. Enjoy!")
        
def process_coin(coffee_type):
    """Ask the user for the coins, and return the calculated monetary value of the coins"""
    print(f"Please insert coins. The {coffee_type}'s cost is: ${MENU[coffee_type]["cost"]}")
    coins = {
        "quarters": int(input("How many quarters?: ")),
        "dimes": int(input("How many dimes?: ")),
        "nickles": int(input("How many nickles?: ")),
        "pennies": int(input("How many pennies?: ")),
    }

    money_payed = round(coins["quarters"] * 0.25 + coins["dimes"] * 0.1 + coins["nickles"] * 0.05 + coins["pennies"] * 0.01, 2)

    return money_payed

def check_transcation(coffee_type, money_payed):
    """Return True if there is enough money to pay for the coffee and add the cost of the coffee to the resources, return False if there is not enough money"""
    coffee_cost = MENU[coffee_type]["cost"]

    if money_payed - MENU[coffee_type]["cost"] >= 0:
        change = money_payed - coffee_cost
        
        if change == 0:
            print(f"You payed the exact price of the {coffee_type}. No change.")

        else:
            print(f"You payed ${money_payed} for the {coffee_type}. Here is your change: ${change}")

        resources["money"] += MENU[coffee_type]["cost"]

        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

machine_on = True
options = ["espresso", "latte", "cappuccino", "report", "off"]

while machine_on:
    # TODO-1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    coffee_machine_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_machine_input in options:
        # TODO-2 Turn off the Coffee Machine by entering “off” to the prompt.
        if coffee_machine_input == "off":
            machine_on = False
        
        # TODO-3 Print report.
        elif coffee_machine_input == "report":
            show_report()

        else:
            # TODO-4 Check resources sufficient?
            if enough_resource(coffee_machine_input):
                # TODO-5 Process coins.
                money = process_coin(coffee_machine_input)
                # TODO-6 Check transaction successful?
                transaction = check_transcation(coffee_machine_input, money)

                if transaction:
                    # TODO-7 Make Coffee.
                    make_coffee(coffee_machine_input)
    else:
        print("Please insert a valid option.")

    print()
