from collections import deque
from dice import Dice
from functions import create_dice, roll_dice, memory

print('This is a Dice Roll game. For a list of commands, type "commands". \n'
      'Begin by creating a new dice. \n')

commands = ("To create a die: create \n"
            "To roll a die or dice: roll \n"
            "To check the previous roll values: memory \n"
            "To see the last 100 values: last \n"
            "To quit the game: exit")

roll_hist = []

while True:
    user_input = input('Enter a command: ')
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.startswith('create'):
        dice = create_dice()
        print('A dice was created! \n')

    elif user_input.startswith('roll'):
        try:
            rolling_dice = roll_dice(dice)
            print(f'Values of dice rolls: {rolling_dice} \n')

        except NameError:
            print('There is nothing to roll. No dice are created! \n')
            continue

    elif user_input.startswith('memory'):
        try:

            last_rolls = memory(roll_hist, rolling_dice)
            print(f'Last roll values: {last_rolls} \n')

        except NameError:
            print('Nothing to remember...\n'
                  'Roll the dice first! \n')
            continue

    elif user_input.startswith('last'):
        try:

            if len(last_rolls) > 100:
                roll_limit = deque(last_rolls, maxlen=100)
                print(f'Last 100 values: {list(roll_limit)}')

            else:
                print('The list contains less than 100 values. \n'
                      'To see current values, type "memory" \n')

        except NameError:
            print('Nothing to remember... Or the list is empty...\n'
                  'Roll the dice first! \n')
            continue

    elif user_input.startswith('commands'):
        print(commands)

    elif user_input.startswith('exit'):
        break

    else:
        print('Unknown command. For the list of commands type "commands" \n')
        continue
