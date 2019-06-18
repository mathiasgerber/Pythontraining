class Item:
    """ Superclass of all items in the game.

    Attributes:
        name (str): Name of the item.
        description (str): Short description what the item is/does.
        value (int): Value the item has when buying or selling it.
    """
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description,
                                                   self.value)


class Gold(Item):
    """ Item that can be found to give the player more gold.

    Attributes:
        amount (int): The amount of gold that is added on pick up.
    """
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold",
                         description="A shiny gold coin.",
                         value=self.amount)


class HealthPotion(Item):
    """ Superclass to specific healing items.

    Attributes:
        healing (int): Amount of Health Points the potion heals.
    """
    def __init__(self, name, description, value, healing):
        self.healing = healing
        super().__init__(name, description, value)


class SmallHealthPotion(HealthPotion):
    """ A Healthpotion that restores 30 Health Points. """
    def __init__(self):
        super().__init__(name="Small Health Potion",
                         description="Restores 20 HP",
                         value=20,
                         healing=30)


class LargeHealthPotion(HealthPotion):
    """ A Healthpotion that restores 50 Health Points. """
    def __init__(self):
        super().__init__(name="Large Health Potion",
                         description="Restores 50 HP",
                         value=40,
                         healing=50)


class Weapon(Item):
    """ Superclass for all Weapons in the game.

    Attributes:
        damage (int): The amount of damage the weapon does to the enemy's
            Health Points.
    """
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name,
                                                             self.description,
                                                             self.value,
                                                             self.damage)


class Stone(Weapon):
    """ A Weapon that deals 5 damage. """
    def __init__(self):
        super().__init__(name="Stone",
                         description="A small stone. You can use it. But well,"
                                     " it doesn't really hurt.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    """ A Weapon that deals 10 damage. """
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger. It's not really a good"
                                     " Weapon, but it's a start.",
                         value=10,
                         damage=10)


class Sword(Weapon):
    """ A Weapon that deals 25 damage. """
    def __init__(self):
        super().__init__(name="Sword",
                         description="An ordinary Sword. Nice to have in an"
                                     " unknown area.",
                         value=20,
                         damage=25)
