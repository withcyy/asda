class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        print(f"Player {self.name}, attacks with damage: {self.damage}")

player = Character("Bob", 100, 50)

player.attack()