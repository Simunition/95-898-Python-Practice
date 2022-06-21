"""Program to roll a variable number of dice with variable number of sides
depending on user input"""
import random


def roll_dice():
    """Repeatable function to roll dice"""
    # Prompt user for number and type of dice, cast to int and then
    # initialize total
    dice_num = int(input("Input the number of dice to roll: "))
    dice_type = int(input("Input the number of sides on the dice, i.e. 20: "))
    dice_sum = 0

    # loop through range based on number of dice user selected,
    # randomly select a roll based on dice type user selected,
    # print roll add new roll to total sum
    for die in range(dice_num):
        roll = random.randint(1, dice_type)
        print(f"Die {die + 1}: {roll}")
        dice_sum += roll

    # print final total
    print(f"Total: {dice_sum}")


# Call function
roll_dice()
