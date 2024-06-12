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

    def __str__(self):
        return f"Inventory: {', '.join(self.inside) if self.inside else 'empty'}"
