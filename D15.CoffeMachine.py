import os

def clear():
    """Clears the screen"""
    os.system('cls')

MENU = {
    "espresso": {
        "name": "espresso",
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "name": "latte",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "name": "cappuccino",
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
        return
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
        print("Ok")
    return count
    
def coffee_machine():
    turn_off = False
    while turn_off != True:
        choice = user_input()
        turn_off = evaluate_answer(choice, turn_off)
        cooking = evaluate_resourses(choice)
        


coffee_machine()
