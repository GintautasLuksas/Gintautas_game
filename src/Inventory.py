class Inventory:
    def __init__(self):
        self.inside = []

    def acquire_item(self, item):
        self.inside.append(item)

    def lose_item(self, item):
        if item in self.inside:
            self.inside.remove(item)
        else:
            print(f"Item '{item}' not found in inventory.")

    def has_item(self, item):
        return item in self.inside

    def equip_item(self, item, player_stats):
        if item in self.inside:
            item.modify_stats(player_stats)
            print(f"Equipped {item} successfully.")
        else:
            print(f"Item '{item}' not found in inventory.")

    def unequip_item(self, item, player_stats):
        if item in self.inside:
            item.revert_stats(player_stats)
            print(f"Unequipped {item} successfully.")
        else:
            print(f"Item '{item}' not found in inventory.")

    def __str__(self):
        return f"Inventory: {', '.join(str(item) for item in self.inside) if self.inside else 'empty'}"