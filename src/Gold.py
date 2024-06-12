class Gold:
    def __init__(self, amount=0):
        self.amount = amount

    def add_gold(self, amount):
        self.amount += amount

    def spend_gold(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Not enough gold.")

    def __str__(self):
        return f"Gold: {self.amount}"
