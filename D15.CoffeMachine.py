import os

def clear():
    """Clears the screen"""
    os.system('cls')

MENU = {
    "espresso": {
        "name": "espresso",
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "name": "latte",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "name": "cappuccino",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources['water']} ml.\nMilk: {resources['milk']} ml.\nCoffe: {resources['coffee']} g.")

def user_input():
    x = input("What would you like? (espresso/latte/cappuccino):")
    if x == "espresso":
        return  MENU["espresso"]
    elif x == "latte":
        return MENU["latte"]
    elif x == "cappuccino":
        return MENU["cappuccino"]
    elif x == "report":
        return "report" 
    elif x == "off":
        return "off"
    else:
        clear()
        user_input()

def evaluate_answer(choice, turn_off):
        if choice == "off":
            turn_off = True
            return turn_off
        elif choice == "report":
            report()
        else:
            print(f"You get a {choice['name']} for {choice['cost']}$")

def evaluate_resourses(choice):
    count = 0
    if choice == "report" or choice == "off":
        return 0
    elif choice["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        count += 1
    elif choice["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        count += 1
    elif choice["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        count += 1
    else:
        print("")
    return count

        
def process_coins(choice):
    try:
        print("Please insert coins.\nQuarters = $0.25, Dimes = $0.10, Nickels = $0.05, Pennies = $0.01")
        quarters = float(input("How many quarters: ")) * 0.25
        dimes = float(input("How many dimes: ")) * 0.10
        nickels = float(input("How many nickels: ")) * 0.05
        pennies = float(input("How many pennies: ")) * 0.01
        total_coins = quarters + dimes + nickels + pennies
        total_amount = ((10 ** 2) * total_coins + 0.5) // 1 / (10 ** 2)

        if input(f"Is this the correct amount {total_amount}$? Type 'y' or 'n': ") == 'n':
            return None  # Return None to indicate an unsuccessful transaction
        else:
            if choice["cost"] <= total_amount:
                change = ((10 ** 2) * (total_amount - choice['cost']) + 0.5) // 1 / (10 ** 2)
                print(f"Your change is {change}$")
                print(f"Enjoy your {choice['name']}!")
            else:
                print(f"That's not enough, needed {choice['cost']}$, inserted {total_amount}$")
                return None  # Return None to indicate an unsuccessful transaction
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None  # Return None to indicate an unsuccessful transaction


def brewing(choice, dic):
    resources["water"] = resources["water"] - choice["ingredients"]['water']
    resources["milk"] = resources["milk"] - choice["ingredients"]['milk']
    resources["coffee"] = resources["coffee"] - choice["ingredients"]['coffee']
    return resources

def coffee_machine():
    turn_off = False
    while not turn_off:
        choice = user_input()
        turn_off = evaluate_answer(choice, turn_off)
        if turn_off:
            break
        cooking = evaluate_resourses(choice)
        if cooking > 0:
            continue  
        coins = process_coins(choice)
        if coins is None:
            continue  
        brewing(choice, resources)
        print(f"Enjoy your hot {choice['name']}!")        


coffee_machine()

