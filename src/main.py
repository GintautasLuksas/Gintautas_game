from src.Stats import Stats
from src.Inventory import Inventory
from src.Gold import Gold
from src.Monsters.base_monster import BaseMonster
import random

player_gold = Gold(100)
player_stats = Stats(100, 100, 25, 15, player_gold)
player_inventory = Inventory()


def main_menu():
    while True:
        user_choice = input('''Welcome! Select option:
        1. New game.
        2. Load game.
        3. Game information.
        4. Quit
        Your choice: ''').lower()
        if user_choice == 'new game':
            new_game()
            return True
        elif user_choice == 'load game':
            load_game()
            return True
        elif user_choice == 'game information':
            game_information()
            return True
        elif user_choice == 'quit':
            print('Quit')
            return True
        else:
            print('Wrong entry. Try again.')
            continue


def save_game():
    # Content to be written to the file
    content = f"""# User stats
HP = {player_stats.hp}
MP = {player_stats.mp}

# User points
STR = {player_stats.str}
AGI = {player_stats.agi}

# Inventory
INVENTORY = {player_inventory}

# Currency
GOLD = {player_stats.gold}
"""
    with open('Saved.txt', 'w') as file:
        file.write(content)
    print("Game saved successfully!")


def load_game():
    global player_stats
    try:
        with open('Saved.txt') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("HP = "):
                    player_stats.hp = int(line.split(" = ")[1].strip())
                elif line.startswith("MP = "):
                    player_stats.mp = int(line.split(" = ")[1].strip())
                elif line.startswith("STR = "):
                    player_stats.str = int(line.split(" = ")[1].strip())
                elif line.startswith("AGI = "):
                    player_stats.agi = int(line.split(" = ")[1].strip())
                elif line.startswith("GEAR = "):
                    player_stats.gear = eval(line.split(" = ")[1].strip())
                elif line.startswith("INVENTORY = "):
                    player_stats.inventory = eval(line.split(" = ")[1].strip())
                elif line.startswith("GOLD = "):
                    player_stats.gold = int(line.split(" = ")[1].strip())
        print("Game loaded successfully!")
        print(player_stats)
    except FileNotFoundError:
        print("No saved game found. Please start a new game.")


def game_information():
    print('''
The game is created for learning purposes.
Any kind of fun bugs can occur while playing.
That is it with information. :) ''')
    main_menu()


def new_game():
    global player_stats
    print("New game started with initial stats:")
    print(player_stats)
    input('Press Enter to continue...')


# Monster Whelp Fight
whelp = BaseMonster('Whelp', 20, 10)
while True:
    attack = random.randint(1, 4)
    user_input = int(input('''
The fight is on. Choose your action:
1. Stay at place, so you can attack.
2. Move left to avoid fire.
3. Move right to avoid it jumping on you.
4. Hide behind rock to avoid flight attack..'''))

    if user_input == 1 and attack == 1:
        print(
            'You hide behind rock, whelp tried to get in the air and hit you with his face, but hit rock. It is dead!')
        whelp.add_loot('Bronze Helm')
        print(f'''
        You defeated the monster and got a Bronze Helm!
        Inventory update: {player_inventory}''')
        break
    elif user_input == 2 and attack == 2:
        print(
            'You hide behind rock, whelp tried to get in the air and hit you with his face, but hit rock. It is dead!')
        whelp.add_loot('Bronze Helm')
        print(f'''
        You defeated the monster and got a Bronze Helm!
        Inventory update: {player_inventory}''')
        break
    elif user_input == 3 and attack == 3:
        print(
            'You hide behind rock, whelp tried to get in the air and hit you with his face, but hit rock. It is dead!')
        whelp.add_loot('Bronze Helm')
        print(f'''
        You defeated the monster and got a Bronze Helm!
        Inventory update: {player_inventory}''')
        break
    elif user_input == 4 and attack == 4:
        print('''You hide behind rock, whelp tried to get in the air and hit you with his face, 
        but hit rock. It is dead!''')
        whelp.add_loot('Bronze Helm')
        print(f'''
You defeated the monster and got a Bronze Helm!
Inventory update: {player_inventory}''')
        break
    else:
        print(f'Oh no! You guessed {user_input} scenario. But the dragon had {attack} scenario!')
        player_stats.hp -= whelp.damage
        print(f'You have {player_stats.hp} left!')
        if player_stats.hp <= 0:
            print("You died!")
            continue


main_menu()
