from src.Gold import Gold
class Stats:
    def __init__(self, HP, MP, STR, AGI, gold_amount):
        self.hp = HP
        self.mp = MP
        self.str = STR
        self.agi = AGI
        self.gold = Gold(gold_amount)

    def __str__(self):
        return (f"HP: {self.hp}, MP: {self.mp}\n"
                f"STR: {self.str}, AGI: {self.agi}\n"
                f"{self.gold}")


