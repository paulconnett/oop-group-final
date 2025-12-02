'''
Room class
'''

__author__ = 'Parker Stacy'

import random
from abc import ABC, abstractmethod
from typing import List
from item import Item, Weapon, Armor, Potion, PotionHP, PotionStrength
from enemy import Enemy
from player import Player


class Room(ABC):
    '''
    Room class
    '''
    def __init__(self, level: int, player: Player):
        self._level = level
        self._player = player

    @abstractmethod
    def play_room(self, player: Player):
        '''
        runs room logic (visit shop/fight monster)
        '''

    @abstractmethod
    def __str__(self) -> str:
        '''
        overload print method
        '''

    @property
    def level(self) -> int:
        '''
        getter for private attribute
        '''
        return self._level


class Shop(Room):
    '''
    shop class
    '''
    TEMP_SHOP: List[Item] = []

    TEMP_SHOP.append(Weapon("Sword", 5, 10))
    TEMP_SHOP.append(Armor("Steel Plate", 10, 20))
    TEMP_SHOP.append(PotionHP("Healing Potion", 5))
    TEMP_SHOP.append(PotionStrength("Strength Potion", 5))

    def __init__(self, level: int, player: Player):
        '''
        constructor
        '''
        super().__init__(level, player)
        self._items: List[Item] = Shop.TEMP_SHOP

    def play_room(self, player: Player) -> None:
        '''
        player enters shop
        '''
        input(f"\nWelcome to Bork's Level {self.level} shop! (Press Enter to continue...)")
        print(self)

        print(f"You have {player.money} c")
        user_in = input("Bork: Can I interest you in my wares? (y/n)")

        if user_in == ('n' or 'N'):
            input("Bork: See you next time... I hope...    (Press Enter)")
            return
        if user_in == ('y' or 'Y'):
            self.buy_items(self._items)

    def buy_items(self, items: List[Item]) -> None:
        '''
        player buys items from shop
        '''
        item = input("\nWhat's catching your eye? (Enter item number...)")
        item = int(item) - 1

        choice = items[item]  # FIXME check for out of bounds index
        if self._player.spend_money(choice.value):
            if isinstance(choice, Weapon):
                self._player.equip_weapon(choice)
            if isinstance(choice, Armor):
                self._player.equip_armor(choice)
            if isinstance(choice, Potion):
                self._player.inventory.append(choice)

            print(f"{self._player.name} bought a {choice.name}!")
            print(f"New balance: {self._player.money}c")
            input("Bork: See ya, sucker!   (Press enter...)")
        else:
            input("You can't afford that! Don't waste my time!  (Press enter...)")
            self.buy_items(items)

    def __str__(self) -> str:
        '''
        prints shop inventory in readable format
        '''
        rtn = ''
        for item in self._items:
            rtn += f"=== {self._items.index(item) + 1} - {item.name}: {item.value}c ===\n"

        return rtn


class Dungeon(Room):
    '''
    dungeon class
    '''
    temp_e: List[Enemy] = []
    c_temp_e: Enemy

    temp_e.append(Enemy("Goblin", 15, 5, 0, 5))
    # temp_e.append(Enemy("Ogre", 50, 15, 10, 100))
    # temp_e.append(Enemy("Dragon", 100, 25, 10, 250))

    def __init__(self, level: int, player: Player):
        '''
        constructor
        '''
        super().__init__(level, player)
        self._enemies: List[Enemy] = Dungeon.temp_e

    def play_room(self, player: Player):
        '''
        player fights a monster
        '''
        enemy_num: int = random.randint(0, len(self._enemies)-1)
        Dungeon.c_temp_e = self._enemies[enemy_num]  # FIXME get monsters from monster.py file

        print(f"\n{player.name} enters the level {self.level} dungeon...")
        input(f"A {Dungeon.c_temp_e.name} has appeared! Time to throw hands!   (Press enter...)")
        self.combat(player, self.c_temp_e)

    def combat(self, player: Player, enemy: Enemy):
        '''
        combat engine
        '''
        while enemy.is_alive:
            print(f"\n===== {player.name} - {player.hp} HP =====")
            print(f"===== {enemy.name} - {enemy.hp} HP =====\n")

            options = ("Attack", "Use potion")
            for o in options:
                print(f"{options.index(o) + 1} - {o}")

            action = input(f"What will the brave {player.name} do?")
            if action == '1':
                dmg = player.attack_entity(enemy)
                print(f"\n{player.name} attacks for {dmg} damage!")

            if action == '2':
                if not player.inventory:
                    print("No potions to use!")
                    self.combat(player, enemy)

                potions: List[Potion] = []
                print("===== Iventory =====")
                for item in player.inventory:
                    if isinstance(item, Potion):
                        potions.append(item)
                        print(f"{potions.index(item) + 1} - {item.name}")

                choice = input(f"Which item will {player.name} use?")
                choice = int(choice) - 1

                player.use_potion(potions[choice])
                print(f"{player.name} used a {potions[choice].name}")

            if enemy.is_alive:
                dmg = enemy.attack_entity(player)
                print(f"\nThe {enemy.name} attacks for {dmg} damage!")

        print(f"\n{enemy.name} has been defeated!")
        player.add_money(enemy.reward)
        print(f"{player.name} gained {enemy.reward} c!")

    def __str__(self) -> str:
        return ''
