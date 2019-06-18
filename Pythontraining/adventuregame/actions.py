from adventuregame.player import Player


class Action:
    """ Class that maps the chosen action to Player methods.

    Attributes:
        method: The corresponding Player method.
        name (str): The name of the Action.
        hotkey (str): The used hotkey to do this action.
        kwargs: The additional arguments that are needed by some actions.
    """
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    """ Class that maps to the move_north method."""
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north',
                         hotkey='n')


class MoveSouth(Action):
    """ Class that maps to the move_south method."""
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south',
                         hotkey='s')


class MoveEast(Action):
    """ Class that maps to the move_east method."""
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
    """ Class that maps to the move_west method."""
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')


class ViewInventory(Action):
    """ Prints the player's inventory """
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory',
                         hotkey='i')


class Attack(Action):
    """ Class that maps to the attack method."""
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey="a",
                         enemy=enemy)


class Flee(Action):
    """ Class that maps to the flee method."""
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey="f",
                         tile=tile)


class Buy(Action):
    """ Class that maps to the buy method."""
    def __init__(self, trader):
        super().__init__(method=Player.buy, name="Trade", hotkey="b",
                         trader=trader)


class Sell(Action):
    """ Class that maps to the sell method."""
    def __init__(self):
        super().__init__(method=Player.sell, name="Sell", hotkey="t")
