from mob import Mob

class Enemy(Mob):
    def __init__(self, name: str, hp: int, attack_value: int, defense: int, reward: int, rank: int):
        super().__init__(name, hp, attack_value, defense)
        self.reward = reward
        self.rank = rank

    def give_money(self) -> int:
