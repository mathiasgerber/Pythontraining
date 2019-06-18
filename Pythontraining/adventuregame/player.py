"""Module for the player class. Implements all actions, the player can do."""


import random
from adventuregame import items
from adventuregame import world


class Player:
    """ The player object contains all the actions a player can make.

    Attributes:
        hp (int): The players Health Points.
        inventory (:obj:'list' of :obj:'Item'): The inventory of the player.
        gold (int): The amount of gold the player has collected.
        location_x (int):  Current position of the player on the x-axis.
        location_y (int): Current position of the player on the y-axis.
        victory (bool): Boolean that is set true as soon as the player has won.
    """

    def __init__(self):
        self.hp = 100
        self.inventory = [items.Stone()]
        self.gold = 15
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        """ Checks if the player is still alive.

        Returns:
            bool: False when player hp is 0 or negative.
        """
        return self.hp > 0

    def print_inventory(self):
        """ Prints the Inventory in the console.

        Returns:
            None
        """
        for item in self.inventory:
            print(item, '\n')
        print("You have {} Gold".format(self.gold))

    def move(self, dx, dy):
        """ Moves the player in the specified direction.

        Args:
            dx (int): Distance of the move on the x-axis.
            dy (int): Distance of the move on the y-axis.

        Returns:
            None
        """
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).entry_text())

    def move_north(self):
        """ Moves the player north.

        Returns:
            None
        """
        self.move(dx=0, dy=-1)

    def move_south(self):
        """ Moves the player south.

        Returns:
            None
        """
        self.move(dx=0, dy=1)

    def move_east(self):
        """ Moves the player east.

        Returns:
            None
        """
        self.move(dx=1, dy=0)

    def move_west(self):
        """ Moves the player west.

        Returns:
            None
        """
        self.move(dx=-1, dy=0)

    def buy(self, trader):
        """ Buys an item from the trader and puts it into the inventory.

        Args:
            trader: The trader the player is interacting with.

        Returns:
            None
        """
        # Shows the inventory of the trader and asks the user to choose one.
        trader.print_inventory()
        item_input = input("Choose an item: ")
        item = None

        # Loops over the inventory of the trader to get the matching item.
        for i in trader.inventory:
            if i.name == item_input:
                item = i

        # If there was a matching item and the player has enough gold, the item
        # is appended to the players inventory. If there's no matching item, or
        # the player doesn't have enough gold, an error message is displayed.
        if item is not None and item.value <= self.gold:
            self.inventory.append(item)
            self.gold -= item.value
            print("You bought {}".format(item.name))
        else:
            print("You can't buy this.")

    def sell(self):
        """ Removes an item from the inventory and adds the item value as gold.

        Returns:
            None
        """
        self.print_inventory()
        item_name = input("Choose item to sell: ")
        item = None

        # Loops over the players inventory to get the matching item.
        for i in self.inventory:
            if i.name == item_name:
                item = i
        # If there was a matching item, the item value gets added to the
        # players gold and the item gets removed. If not, an error message
        # is displayed.
        if item is not None:
            self.gold += item.value
            self.inventory.remove(item)
            print("You sold {}".format(item.name))
        else:
            print("You don't have this Item.")

    def attack(self, enemy):
        """ Deals damage to the enemy in this rooms.

        Args:
            enemy: The enemy the player is fighting.

        Returns:
            None
        """
        weapon = None
        max_dmg = 0

        # Takes the Weapon with the most Damage in the inventory.
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    weapon = i

        print("You attack with {}. {} takes {} Damage.".format(weapon.name,
                                                               enemy.name,
                                                               max_dmg))

        # Removes the damage the player's attack did from the hp of the enemy
        # and displays the enemy's remaining hp, or reports his death.
        enemy.hp = enemy.hp - max_dmg
        if enemy.is_alive():
            print("{} has {} HP remaining.".format(enemy.name,
                                                   enemy.hp))
        else:
            print("{} has been defeated.".format(enemy.name))

    def flee(self, tile):
        """ Moves the player randomly to an adjacent room.

        Returns:
            None
        """
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def do_action(self, action, **kwargs):
        """ Maps the choosen Action object to the right player action.

        Takes the name of the Method from the Action object. Then the matching
        player method gets executed.
        Args:
            action: The Action object in which the matching player method is
                saved.
            **kwargs: The argument that the specific player action requires,
                for example trader for the actions buy and sell.

        Returns:
            None
        """
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
