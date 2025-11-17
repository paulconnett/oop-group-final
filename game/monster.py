from enemy import Enemy

def monsters():
    """10 monsters. One for each level
    """
    return [
        Enemy("Slime", 30, 5, 0, 10),
        Enemy("Wolf", 40, 7, 1, 15),
        Enemy("Goblin", 60, 10, 3, 20),
        Enemy("Skeleton", 55, 12, 2, 22),
        Enemy("Bandit", 70, 14, 4, 25),
        Enemy("Orc", 80, 16, 5, 30),
        Enemy("Wraith", 100, 18, 8, 35),
        Enemy("Ogre", 130, 20, 10, 40),
        Enemy("Giant", 150, 25, 12, 45),
        Enemy("Dragon", 200, 30, 15, 100)
    ]
