class Stats:
    def __init__(self, HP, MP, STR, AGI, GEAR, GOLD):
        self.hp = HP
        self.mp = MP
        self.str = STR
        self.agi = AGI
        self.gear = GEAR
        self.gold = GOLD

    def __str__(self):
        return (f"HP: {self.hp}, MP: {self.mp}\n"
                f"STR: {self.str}, AGI: {self.agi}\n"
                f"GEAR: {self.gear}\n"
                f"GOLD: {self.gold}")
