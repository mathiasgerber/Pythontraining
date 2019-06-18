from adventuregame import items, enemies, actions, world, npc


class RoomTile:
    """ Superclass for all the different rooms.

    Attributes:
        x (int): Room coordinate on the x-axis.
        y (int): Room coordinate on the y-axis.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def entry_text(self):
        """ Prints an entry text whenever a room is entered. """
        raise NotImplementedError()

    def modify_player(self, player):
        """ Modifies the player depending on the room."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """ Checks if there are adjacent RoomTiles to move to.

        Returns:
            moves (:obj:'List' of :obj:'Actions'): Returns possible moves that
                can be made from this Room to another.
        """
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """ Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves


class LootRoom(RoomTile):
    """ Superclass for all Loot-Type rooms in which the player gains something

    Attributes:
        item (:obj:'Item'): The Item that is picked up in this room.
        lootable (bool): Bool that defines if the item has already been picked
            up or not.
    """
    def __init__(self, x, y, item):
        self.item = item
        self.lootable = True
        super().__init__(x, y)

    def add_loot(self, player):
        """ Adds the lootable item to the players inventory. """
        player.inventory.append(self.item)

    def modify_player(self, player):
        """ If the item is still available, starts the add_loot method. """
        if self.lootable:
            self.add_loot(player)
            self.lootable = False
        pass


class DaggerRoom(LootRoom):
    """ A LootRoom in which a Dagger can be found. """
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def entry_text(self):
        if self.lootable:
            return "There's a small, shining Dagger on the Ground."
        else:
            return "Nothing remains here."


class Find5GoldRoom(LootRoom):
    """ A LootRoom in which Gold can be found. """
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def entry_text(self):
        if self.lootable:
            return "You find a shiny Gold Coin on the floor."
        else:
            return "Nothing remains here."

    def add_loot(self, player):
        player.gold += self.item.amount


class EnemyRoom(RoomTile):
    """ Superclass for Rooms with an enemy in it.

    Attributes:
        enemy (:obj:'Enemy'): The enemy object in this room.
    """
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        """ Modifies the players Health Points from the attack of the enemy."""
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The {} does {} Damage to you. You have {} HP remaining."
                  .format(self.enemy.name, self.enemy.damage, player.hp))

    def available_actions(self):
        """ Chooses the available actions depending on the enemy's status."""
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            return moves


class OgreRoom(EnemyRoom):
    """ EnemyRoom with an Ogre as enemy."""
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def entry_text(self):
        if self.enemy.is_alive():
            return "A tall Ogre stands in your Way."
        else:
            "The rotting Ogre still lies on the ground."


class WolfRoom(EnemyRoom):
    """ EnemyRoom with a Wolf as Enemy."""
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def entry_text(self):
        if self.enemy.is_alive():
            return "A wolf jumps right upon you."
        else:
            "The corpse of a Wolf lies here."


class ZombieRoom(EnemyRoom):
    """ EnemyRoom with a Zombie as Enemy."""
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def entry_text(self):
        if self.enemy.is_alive():
            return "A Zombie slowly walks into your direction."
        else:
            "The headless corpse is still rotting away on the ground."


class EmptyRoom(RoomTile):
    """ Default Room for empty rooms."""
    def entry_text(self):
        return "There is nothing here."

    def modify_player(self, player):
        pass


class StartingRoom(RoomTile):
    """ The Room in which the game starts."""
    def entry_text(self):
        return "Your eyes slowly adapt to the darkness. You find yourself " \
               "in a cave. Around you seem to be four paths."

    def modify_player(self, player):
        pass


class TraderRoom(RoomTile):
    """ Superclass for Rooms with a trader in it.

    Attributes:
        trader (:obj:'NPC'): A trader npc to buy and sell items.
    """
    def __init__(self, x, y, trader):
        self.trader = trader
        super().__init__(x, y)

    def modify_player(self, player):
        pass

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Buy(trader=self.trader))
        moves.append(actions.Sell())
        return moves


class WeaponRoom(TraderRoom):
    """ A TraderRoom with a Weapontrader in it."""
    def __init__(self, x, y):
        super().__init__(x, y, npc.WeaponTrader())

    def entry_text(self):
        return "You see Jill the Weapon Trader."


class ItemRoom(TraderRoom):
    """ A TraderRoom with an Itemtrader in it."""
    def __init__(self, x, y):
        super().__init__(x, y, npc.ItemTrader())

    def entry_text(self):
        return "You see Marc the Item Trader."


class HealingRoom(RoomTile):
    """ A Room which heals the player to full life."""
    def entry_text(self):
        return "You feel a healing Power flow through you. You get fully" \
               " healed."

    def modify_player(self, player):
        player.hp = 100


class CaveExit(RoomTile):
    """ The Room with which the game ends as soon as the player reaches it."""
    def entry_text(self):
        return "You find an exit to the cave. Be happy."

    def modify_player(self, player):
        player.victory = True
