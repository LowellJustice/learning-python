import random


def ask_for_input():
    value = input("Would you like to go again? Press \'1\' for yes and \'2\'" +
                  "for no: ")
    if (value.strip() == '1'):
        roll_dice()

    if (value.strip() != '2'):
        print("Incorrect input. Try again")
        ask_for_input()


def roll_dice():
    print(random.randint(1, 6))
    ask_for_input()


roll_dice()
