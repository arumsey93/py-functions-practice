def calc_dollars():
    piggy_bank = {
        "quarters": 4,
        "dimes": 5,
        "nickels": 10,
        "pennies": 50
    }
    dollar_amount = 0
    for (x, y) in piggy_bank.items():
        if x == "quarters":
            dollar_amount += y * .25
        elif x == "dimes":
            dollar_amount += y * .10
        elif x == "nickels":
            dollar_amount += y * .05
        else:
            dollar_amount += y * .01

    new_amount = f"{round(dollar_amount, 2): .2f}"
    print(f"${new_amount}")

calc_dollars()


        


