from mob import Mob
from item import Weapon, Armor, Potion

class Player(Mob):
    def __init__(self, name: str):
        super().__init__(name, hp=100, attack_value=10, defense=5)
        self.money = 0
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.potion = None

    def pick_up_item(self, item):

    def use_potion(self, potion: Potion):

    def equip_weapon(self, weapon: Weapon):

    def equip_armor(self, armor: Armor):
