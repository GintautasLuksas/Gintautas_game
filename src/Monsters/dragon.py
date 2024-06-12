from base_monster import BaseMonster

class Dragon(BaseMonster):
    def __init__(self):
        super().__init__(name="Dragon", life=100, damage=20)
        self.fly_speed = 20  # Specific to dragons
        self.breath_attack = True  # Specific to dragons

    def fire_breath_attack(self, target):
        damage_multiplier = 2  # Adjust multiplier as needed
        damage_dealt = int(self.damage * damage_multiplier)
        target.take_damage(damage_dealt)
        print(f"The {self.name} unleashes a torrent of fire, dealing {damage_dealt} damage to you!")

    def flying_strike(self, target):
        damage_dealt = self.damage
        target.take_damage(damage_dealt)
        print(f"The {self.name} swoops down and strikes you, dealing {damage_dealt} damage!")

    def dragon_roar(self, target):
        # Implement roar effects such as stunning or intimidation
        print(f"The deafening roar of the {self.name} echoes through the battlefield!")
