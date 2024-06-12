class BaseMonster:
    def __init__(self, name: str, life: int, damage: int):
        self.name = name
        self.life = life
        self.damage = damage
        self.loot_items = []

    def take_damage(self, amount: int):
        self.life -= amount
        if self.life <= 0:
            self.life = 0
            print(f"{self.name} has been defeated!")

    def attack(self, target):
        target.take_damage(self.damage)

    def add_loot(self, item: str):
        self.loot_items.append(item)

    def drop_loot(self, inventory):
        for item in self.loot_items:
            inventory.acquire_item(item)
        self.loot_items.clear()

    def __str__(self):
        return f"Monster: {self.name}, Life: {self.life}, Damage: {self.damage}"
