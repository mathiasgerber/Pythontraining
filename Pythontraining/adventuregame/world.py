"""Module in which the World space is loaded from map.txt."""


_world = {}
starting_position = (0, 0)


def load_tiles():
    """ Parses a file that puts the world space into the _world object

    Returns:
        None
    """
    with open('C:/Users/I0319914/PycharmProjects/Pythontraining/Resources/map.'
              'txt', 'r') as f:
        rows = f.readlines()

    # Loop over the rows of the textfile. Same amount ob Tabs expected on each
    # line
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')

        #
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(
                __import__('rooms'), tile_name)(x, y)


def tile_exists(x, y):
    """ Returns the room at position (x, y), or none, if there is no room.

    Args:
        x (int): x-Coordinate in the Worldspace.
        y (int): y-Coordinate in the Worldspace.

    Returns:
        room (:obj: 'RoomTile'): The room at position (x, y).
    """
    return _world.get((x, y))
