#!/usr/bin/env python

import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("dice_shorthand", help="Die or Dice to be rolled, in the format <amount>d<sides> For example, 1d20 == roll a single, twenty-sided die")

args = parser.parse_args()

def mod_roll(number, max_value):
    return (number % max_value) + 1

def roll(count = None, range = -1):
    random = os.urandom(count)
    numbers = map(ord, random)
    roll_results = [mod_roll(n, range) for n in numbers]
    print roll_results

def usage():
    dice_shorthand = None

    if args.dice_shorthand:
        dice_shorthand = args.dice_shorthand
        (count, sides) = dice_shorthand.split("d")
        roll(int(count), int(sides))

usage()