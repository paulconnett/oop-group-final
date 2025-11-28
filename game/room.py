'''
Room class
'''

__author__ = 'Parker Stacy'

import random
from abc import ABC, abstractmethod
from typing import List
from item import Item
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

    TEMP_SHOP.append(Item("Sword", 5))
    TEMP_SHOP.append(Item("Axe", 10))
    TEMP_SHOP.append(Item("Potion", 3))

    def __init__(self, level: int, player: Player):
        '''
        constructor
        '''
        super().__init__(level, player)
        self._items: List[Item] = Shop.TEMP_SHOP

    def play_room(self) -> None:
        '''
        player enters shop
        '''
        input(f"Welcome to Bork's Level {self.level} shop! (Press Enter to continue...)")
        print(self)

        print(f"You have {self._player.money} c")  # FIXME need a getter method here
        user_in = input("Bork: Can I interest you in my wares? (y/n)")

        if user_in == 'n':
            input("Bork: See you next time... I hope...    (Press Enter)")
            return
        elif user_in == 'y':
            self.buy_items(self._items)

    def buy_items(self, items: List[Item]) -> None:
        item = input("What's catching your eye? (Enter item number 1,2,...)")
        item = int(item)

        choice = items[item + 1]
        if self._player.spend_money(choice.value):
            input(f"You bought a {choice.name}!\nBork: See ya sucker!   (Press enter...)")

    def __str__(self) -> str:
        '''
        prints shop inventory in readable format
        '''
        rtn = ''
        i = 1

        for item in self._items:
            rtn += f"=== {i} - {item.name}: {item.value} ===\n"
            i += 1

        return rtn


class Dungeon(Room):
    '''
    dungeon class
    '''
    temp_e: List[Enemy] = []
    c_temp_e: Enemy

    temp_e.append(Enemy("Goblin", 10, 5, 0, 5))
    temp_e.append(Enemy("Ogre", 50, 15, 10, 100))
    temp_e.append(Enemy("Dragon", 100, 25, 10, 250))

    def __init__(self, level: int, player: Player):
        '''
        constructor
        '''
        super().__init__(level, player)
        self._enemies: List[Enemy] = Dungeon.temp_e

    def play_room(self, player: Player):
        enemy_num: int = random.randint(0, len(self._enemies)-1)
        Dungeon.c_temp_e = self._enemies[enemy_num]  # FIXME get monsters from monster.py file

        print(f"A {Dungeon.c_temp_e.name} has appeared! Time to throw hands!")

    def combat(self, player: Player, enemy: Enemy):
        options = ["Attack", "Use potion"]
        for i in range(len(options)-1):
            print(f"{i+1} - {options[i]}")

        action = input(f"What will the brave {self._player.name} do?")
        if action == '1':
            dmg = self._player.attack_entity(Dungeon.c_temp_e)
            print(f"{self._player.name} attacks for {dmg} damage!")
        if action == '2':
            pass
            # self._player.use_potion(potion=)

            # FIXME need access to player inventory, potion system is weird, but my branch
            # might not be up to date. Stay tuned...

    def __str__(self) -> str:
        return ''
