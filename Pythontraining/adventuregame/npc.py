from adventuregame import items


class Npc:
    """ Superclass for all NPCs in the game.

    Attributes:
        name (str): The name of the NPC.
        hp (str): Health Points of the NPC.
    """
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Trader(Npc):
    """ Superclass of trader NPCs in the game.

    Attributes (:obj:'list' of :obj:'Item'
    """
    def __init__(self, name, hp, inventory):
        self.inventory = inventory
        super().__init__(name, hp)

    def print_inventory(self):
        """ Prints the inventory of the trader. """
        for item in self.inventory:
            print(item, '\n')


class WeaponTrader(Trader):
    """ Trader that trades weapons."""
    def __init__(self):
        super().__init__(name="Trader Jill",
                         hp=15,
                         inventory=[items.Sword(), items.Dagger()])


class ItemTrader(Trader):
    """ Trader that trades Health Potions."""
    def __init__(self):
        super().__init__(name="Trader Marc",
                         hp=20,
                         inventory=[items.SmallHealthPotion(),
                                    items.LargeHealthPotion()])
