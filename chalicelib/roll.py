import os, secrets

def mod_roll(number, max_value):
    return (number % max_value) + 1

def roll(count = None, sides = -1):
    roll_results = []
    for i in range(count):
        roll_results.append(secrets.randbelow(sides) + 1)

    return roll_results

def stringify(rolls = None):
    rollStr = ""
    for roll in rolls:
        rollStr = rollStr + str(roll) + ", "

    return "You rolled: " + rollStr[:-2]

def parse_shorthand(dice_shorthand = None):
    (count, sides) = dice_shorthand.split("d")
    results = roll(int(count), int(sides))
    return stringify(results)
