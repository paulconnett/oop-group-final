'''
Game driver class
'''

__author__ = 'Parker Stacy'

from typing import List
from room import Room, Shop, Dungeon
from player import Player


class Game():
    '''
    game driver class
    '''
    NUM_LEVELS = 10

    def __init__(self) -> None:
        '''
        constructor
        '''
        self._rooms: List[Room] = []
        self._player: Player = Player("Player_Name")

        for i in range(Game.NUM_LEVELS):
            shop = Shop(i+1, self._player)
            self._rooms.append(shop)
            dun = Dungeon(i+1, self._player)
            self._rooms.append(dun)

    def play_game(self) -> None:
        '''
        runs game logic
        '''
        input("Welcome to the Dungeon >:)   (Press Enter to continute...)")
        rooms: List[Room] = self._rooms

        for curr_room in rooms:
            curr_room.play_room(self.player)

        print("Game Over!")

    @property
    def player(self) -> Player:
        '''
        returns the current player object
        '''
        return self._player

    @staticmethod
    def main() -> None:
        '''
        main method
        '''
        game = Game()
        game.play_game()


if __name__ == '__main__':
    Game.main()
