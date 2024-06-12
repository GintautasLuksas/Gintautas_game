from base_monster import BaseMonster

class Beast(BaseMonster):
    def __init__(self):
        super().__init__(name="Beast", life=75, damage=15)
        self.speed = 15
        self.roar = True

    def roar_attack(self, target):
        damage_multiplier = 1.5
        damage_dealt = int(self.damage * damage_multiplier)
        target.take_damage(damage_dealt)
        print(f"The {self.name} unleashes a powerful roar, dealing {damage_dealt} damage to you!")

    def charge_attack(self, target):
        damage_dealt = self.damage
        target.take_damage(damage_dealt)
        print(f"The {self.name} charges at you, dealing {damage_dealt} damage!")

    def rage_mode(self):
        damage_multiplier = 2
        self.damage *= damage_multiplier
        print(f"The {self.name} enters rage mode, increasing its damage output!")

    def end_rage_mode(self):
        damage_multiplier = 0.5
        self.damage = int(self.damage * damage_multiplier)
        print(f"The {self.name} calms down from rage mode, returning its damage output to normal.")
