from base_monster import BaseMonster
import random

class Goblin(BaseMonster):
    def __init__(self):
        super().__init__(name="Goblin", life=30, damage=5)
        self.stealth = 10  # Specific to goblins
        self.hide = True   # Specific to goblins

    def banana_peel_slip(self, target):
        slip_chance = 0.5  # Chance of slipping on banana peel
        if random.random() < slip_chance:
            print(f"The {self.name} tosses a banana peel, causing you to slip and fall!")
            target.immobilize()
        else:
            print(f"The {self.name} tries to throw a banana peel, but misses!")

    def sneaky_pickpocket(self, target):
        # Simulate pickpocketing by randomly removing an item from the target's inventory
        if target.inventory:
            item_stolen = random.choice(target.inventory)
            target.lose_item(item_stolen)
            print(f"The {self.name} sneakily pickpockets {item_stolen} from you!")
        else:
            print("The goblin attempts to pickpocket, but finds nothing of value in your inventory!")

    def goblin_dance_party(self):
        # Implement distraction effects such as lowering target's defense or evasion
        print("The goblin starts a spontaneous dance party, distracting you from the fight!")
