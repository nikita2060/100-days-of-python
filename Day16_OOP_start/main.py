from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:  # program will run until user gives input to turn off
    menu = Menu()
    user_choice = input(f"What would you like? {menu.get_items()}")
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    if user_choice == "report":  # TODO-Done:1.Print report
        coffee_maker.report()    # gives report of ingredients
        money_machine.report()  # gives report of money
    elif user_choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):  # TODO-Done:2.Check resources sufficient or not
            if money_machine.make_payment(drink.cost):  # TODO-Done:3.Process coins and Check transaction is # successful or not
                coffee_maker.make_coffee(drink) # TODO-Done:4.Make Coffee

