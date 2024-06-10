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
