'''
Room class
'''

__author__ = 'Parker Stacy'

import random
from abc import ABC, abstractmethod
from typing import List
from item import Item
from enemy import Enemy


class Room(ABC):
    '''
    Room class
    '''
    def __init__(self, level: int):
        self._level = level

    @abstractmethod
    def play_room(self):
        '''
        runs room logic (visit shop/fight monster)
        '''

    @abstractmethod
    def print(self):
        '''
        display upon entering the room
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
    temp_shop: List[Item] = []

    temp_shop.append(Item("Sword", 5))
    temp_shop.append(Item("Axe", 10))
    temp_shop.append(Item("Potion", 3))

    def __init__(self, level: int):
        '''
        constructor
        '''
        super().__init__(level)
        # self._num_items: int = 5  # Can be adjusted later
        # self._items: List[Item] = []
        # self._num_items: int = len(Shop.temp_shop)
        self._items: List[Item] = Shop.temp_shop

    def play_room(self):
        '''
        player enters shop
        '''
        self.print()

    def print(self):
        '''
        prints shop inventory in readable format
        '''
        print(f"Level {self.level} Shop")
        for item in self._items:
            print(f"=== {item.name}: {item.value} ===")


class Dungeon(Room):
    '''
    dungeon class
    '''
    temp_e: List[Enemy] = []
    c_temp_e: Enemy = None

    temp_e.append(Enemy("Goblin", 10, 5, 0, 5, 0))
    temp_e.append(Enemy("Ogre", 50, 15, 10, 100, 3))
    temp_e.append(Enemy("Dragon", 100, 25, 10, 250, 5))

    def __init__(self, level: int):
        '''
        constructor
        '''
        super().__init__(level)
        self._enemies: List[Enemy] = Dungeon.temp_e

    def play_room(self):
        enemy_num: int = random.randint(0, len(self._enemies)-1)
        Dungeon.c_temp_e = self._enemies[enemy_num]
        self.print()

        # This is where combat will happen

    def print(self):
        print(f"Level {self.level} Dungeon")
        print(f"A {Dungeon.c_temp_e.name} has appeared! Time to throw hands!")
