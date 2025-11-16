class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


class Weapon(Item):
    def __init__(self, name: str, value: int, attack_value: int):
        super().__init__(name, value)
        self.attack_value = attack_value


class Armor(Item):
    def __init__(self, name: str, value: int, defense: int):
        super().__init__(name, value)
        self.defense = defense


class Potion(Item):
    def __init__(self, name: str, value: int, potion_type: str):
        super().__init__(name, value)
        self.potion_type = potion_type

    def use(self, target):
        pass


class PotionHP(Potion):
    def __init__(self, name: str, value: int, heal_value: int):
        super().__init__(name, value, potion_type="HP")
        self.heal_value = heal_value

    def use(self, target):
        pass


class PotionStrength(Potion):
    def __init__(self, name: str, value: int, buff: int):
        super().__init__(name, value, potion_type="Strength")
        self.buff = buff

    def use(self, target):
        pass
