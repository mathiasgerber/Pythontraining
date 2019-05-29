import npc


class Enemy(npc.Npc):
    def __init__(self, name, hp, damage):
        self.damage = damage
        super().__init__(name, hp)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",
                         hp=30,
                         damage=15)


class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie",
                         hp=15,
                         damage=5)


class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf",
                         hp=20,
                         damage=10)
