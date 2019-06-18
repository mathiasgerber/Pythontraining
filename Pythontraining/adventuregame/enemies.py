class Enemy:
    """ The super class of all enemytypes in the game.

    Attributes:
        name (str): Name of the enemy.
        hp (int): Remaining Healt Points of the enemy.
        damage (int): Damage Value the enemy does to the player.
    """
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Ogre(Enemy):
    """ Enemy of the Type Ogre. """
    def __init__(self):
        super().__init__(name="Ogre",
                         hp=50,
                         damage=20)


class Zombie(Enemy):
    """ Enemy of the Type Zombie. """
    def __init__(self):
        super().__init__(name="Zombie",
                         hp=15,
                         damage=5)


class Wolf(Enemy):
    """ Enemy of the Type Wolf."""
    def __init__(self):
        super().__init__(name="Wolf",
                         hp=20,
                         damage=10)
