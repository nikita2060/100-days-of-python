MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

ingredients = ["water", "milk", "coffee"]


def get_user_choice():
    """takes user input and returns it"""
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return user_choice


profit = 0


# TODO :1.print report

def report():
    """returns current values of resources in given format"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney:{profit}"


# TODO :2.Check resources are sufficient or not
def sufficient_resource(user_choice):
    """returns true if resource is sufficient else returns false and prints the problem"""
    global ingredients
    for i in ingredients:
        if resources[i] < MENU[f"{user_choice}"]["ingredients"][str(i)]:
            print(f"Sorry,{i} is insufficient\n")
            return False
    return True


# TODO :3.Process coins
def process_coins():
    """calculates total amount of the coins inserted and returns value in dollars"""
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.10
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


# TODO :4.Check transaction successful or not
def check_transaction_is_successful(drink_cost, user_money):
    """returns true if transaction is successful,takes cost of drink and profit(updates profit) ,if money is not sufficient refund it ,if more than required
    then offer change"""
    if drink_cost <= user_money:
        change = round(user_money - drink_cost, 2)
        global profit
        profit += drink_cost
        if change != 0.00:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO :5.Make coffee and deduct quantities
def deduct_quantities(user_choice):
    global ingredients
    for item in ingredients:
        resources[item] -= MENU[f"{user_choice}"]["ingredients"][f"{item}"]


on = 1
while on:
    user_choice = get_user_choice()
    if user_choice == "report":
        print(report())
    elif user_choice == "off":
        on = 0
    else:
        if sufficient_resource(user_choice):
            user_money = process_coins()
            if check_transaction_is_successful(MENU[f"{user_choice}"]["cost"], user_money):
                deduct_quantities(user_choice)
                print(f"Here is your {user_choice} ☕️. Enjoy!")

