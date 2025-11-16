'''
Game driver class
'''

__author__ = 'Parker Stacy'

from typing import List
from room import Room, Shop, Dungeon


class Game():
    '''
    game driver class
    '''
    def __init__(self) -> None:
        '''
        constructor
        '''
        self._num_levels: int = 10
        self._rooms: List[Room] = []

        for i in range(self._num_levels):
            shop = Shop(i+1)
            self._rooms.append(shop)
            dun = Dungeon(i+1)
            self._rooms.append(dun)
            print(f"Level {i+1} created!")

        # Need player, etc from other modules

    def play_game(self) -> None:
        '''
        runs game logic
        '''
        print("Start game!")
        rooms: List[Room] = self._rooms

        for curr_room in rooms:
            curr_room.play_room()

            print("Game Over!")

    @staticmethod
    def main() -> None:
        '''
        main method
        '''
        game = Game()
        game.play_game()


if __name__ == '__main__':
    Game.main()
