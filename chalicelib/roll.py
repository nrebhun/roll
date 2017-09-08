import os

def mod_roll(number, max_value):
    return (number % max_value) + 1

def roll(count = None, range = -1):
    random = os.urandom(count)
    numbers = map(ord, random)
    roll_results = [mod_roll(n, range) for n in numbers]
    return roll_results

def stringify(rolls = None):
    string = ""
    for roll in rolls:
        string = string + str(roll) + ", "

    return "You rolled: " + string[:-2]


def parse_shorthand(dice_shorthand = None):
    (count, sides) = dice_shorthand.split("d")
    results = roll(int(count), int(sides))
    return stringify(results)