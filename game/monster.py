'''
Docstring for game.monster
'''
from typing import List
from enemy import Enemy


def monsters(index: int) -> Enemy:
    """10 monsters. One for each level
    """
    monster_list: List[Enemy] = [
        Enemy("Slime", 10, 5, 0, 10),
        Enemy("Wolf", 15, 7, 1, 15),
        Enemy("Goblin", 25, 10, 3, 20),
        Enemy("Skeleton", 40, 12, 2, 22),
        Enemy("Bandit", 60, 14, 4, 25),
        Enemy("Orc", 80, 16, 5, 30),
        Enemy("Wraith", 100, 18, 8, 35),
        Enemy("Ogre", 130, 20, 10, 40),
        Enemy("Giant", 160, 25, 12, 45),
        Enemy("Dragon", 200, 30, 15, 100)
    ]

    return monster_list[index]
