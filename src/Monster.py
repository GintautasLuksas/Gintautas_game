class Monster:
    def __init__(self, name: str, life: int, damage: int):
        self.name = name
        self.life = life
        self.damage = damage

    def attack(self, hit_to_monster):
        self.life -= hit_to_monster

    def loot(self, inventory, item):
        inventory.append(item)