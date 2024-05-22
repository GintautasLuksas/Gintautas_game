
class Stats:
    def __init__(self, HP, MP, STR, AGI, GEAR, INVENTORY, GOLD):
        self.hp = HP
        self.mp = MP
        self.str = STR
        self.agi = AGI
        self.gear = GEAR
        self.inventory = INVENTORY
        self.gold = GOLD

    def __str__(self):
        return (f"HP: {self.hp}, MP: {self.mp}\n"
                f"STR: {self.str}, AGI: {self.agi}\n"
                f"GEAR: {self.gear}\n"
                f"INVENTORY: {self.inventory}\n"
                f"GOLD: {self.gold}")

# Initialize global player stats
player_stats = Stats(100, 100, 10, 5, ['Leather gloves', 'Leather boots', 'Leather armor', 'Bronze sword'], [], 0)

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

def save_game(player_stats):
    # Content to be written to the file
    content = f"""# User stats
HP = {player_stats.hp}
MP = {player_stats.mp}

# User points
STR = {player_stats.str}
AGI = {player_stats.agi}

# Gear
GEAR = {player_stats.gear}
INVENTORY = {player_stats.inventory}

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
    player_stats = Stats(100, 100, 10, 5, ['Leather gloves', 'Leather boots', 'Leather armor', 'Bronze sword'], [], 0)
    print("New game started with initial stats:")
    print(player_stats)
    input('Press Enter to continue...')

main_menu()


