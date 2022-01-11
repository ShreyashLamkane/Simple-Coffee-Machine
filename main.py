from data import MENU
from data import resources

coins = 0




def reduce(demand_got):
    resources["water"] = resources["water"] - MENU[demand_got]['ingredients']["water"]
    resources['milk'] = resources['milk'] - MENU[demand_got]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[demand_got]['ingredients']['coffee']


def show():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Coins: {coins}")


def check_resources(check):
    check_temp = MENU[check]['ingredients']
    if check_temp['water'] <= resources['water'] and check_temp['milk'] <= resources['milk'] and check_temp['coffee'] <= \
            resources['coffee']:

        return True
    else:
        if check_temp['water'] <= resources['water']:
            print("Not sufficient water, please refill.")
        elif check_temp['milk'] <= resources['milk']:
            print("Not sufficient milk, please refill.")
        else:
            print("Not sufficient coffee, please add more.")
        return False


def coins_count(coffee_check):
    quarter = int(input("How many Quarters? "))
    dimes = int(input("How many Dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    dollar = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    global coins
    coins = coins + dollar
    print(dollar)
    if dollar == MENU[coffee_check]['cost']:
        return True
    elif dollar >= MENU[coffee_check]['cost']:
        temp = dollar - MENU[coffee_check]['cost']
        print(f"Here is you change: {temp}")
        return True
    else:
        print("Not sufficient coins.")
        return False


# TODO.1:Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

demand = ''
while demand != 'off':
    # TODO.2:Turn off the Coffee Machine by entering “off” to the prompt.
    demand = input('What would you like? (espresso/latte/cappuccino): ')

    # TODO.3:Print report
    if demand == 'report':
        show()
    # TODO.4:Check resources sufficient?
    elif demand == 'espresso' or demand == 'latte' or demand == 'cappuccino':
        coins_check = check_resources(demand)

        # TODO.5:Process coins.
        if coins_check:
            # TODO.6:Check transaction successful?
            operate = coins_count(demand)
            if operate is True:
                reduce(demand)
                # TODO.7:Make Coffee.
                print(f"Here is your {demand} ☕.")
