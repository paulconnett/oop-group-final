class Mob:
    def __init__(self, name: str, hp: int, attack_value: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack_value = attack_value
        self.defense = defense
        self.is_dead = False

    def attack(self, target: "Mob") -> None:
        pass

    def die(self) -> None:
        pass
