class Item:
    def __init__(self, name, stat_modifiers):
        self.name = name
        self.stat_modifiers = stat_modifiers  # Dictionary of stat modifications

    def modify_stats(self, player_stats):
        for stat, value in self.stat_modifiers.items():
            setattr(player_stats, stat, getattr(player_stats, stat) + value)

    def revert_stats(self, player_stats):
        for stat, value in self.stat_modifiers.items():
            setattr(player_stats, stat, getattr(player_stats, stat) - value)

    def __str__(self):
        return self.name

# Creating 10 items
sword = Item("Sword", {"str": 5})
shield = Item("Shield", {"hp": 20})
helmet = Item("Helmet", {"mp": 10})
boots = Item("Boots", {"agi": 7})
armor = Item("Armor", {"hp": 30, "str": -2})
ring_of_power = Item("Ring of Power", {"mp": 15, "str": 3})
amulet_of_health = Item("Amulet of Health", {"hp": 50})
gloves_of_agility = Item("Gloves of Agility", {"agi": 10})
cloak_of_invisibility = Item("Cloak of Invisibility", {"agi": 5, "str": -1})
magic_staff = Item("Magic Staff", {"mp": 25, "str": 2})