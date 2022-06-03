MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

is_machine_on = True

# TODO 5. Process coins.


def do_coffee():
    quarters = int(input("Please insert coins.\nhow many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    user_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    # TODO 6. Check transaction successful?
    if user_money >= MENU[user_decision]["cost"]:
        resources["money"] += MENU[user_decision]["cost"]
        change = round(user_money - MENU[user_decision]["cost"], 2)
        # TODO 7. Make Coffee.
        resources["water"] -= MENU[user_decision]["ingredients"]["water"]
        resources["milk"] -= MENU[user_decision]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_decision]["ingredients"]["coffee"]
        print(f"Here is ${change} in change.\nHere is your {user_decision} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


while is_machine_on:

    # TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    user_decision = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_decision == "off":
        is_machine_on = False
    # TODO 3. Print report.
    elif user_decision == "report":
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')

    # TODO 4. Check resources sufficient?
    elif MENU[user_decision]["ingredients"]["water"] < resources["water"]:
        if MENU[user_decision]["ingredients"]["milk"] < resources["milk"]:
            if MENU[user_decision]["ingredients"]["coffee"] < resources["coffee"]:
                do_coffee()
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")

# # Improving function skills:
#
def function(a, b):
    if a > b:
        return True
    else:
        return False


def function2(a, b):
    return a > b


print(function(5, 4))
print(function2(5, 4))

