import unittest
from adventuregame import world, rooms


class TestWorldMethods(unittest.TestCase):

    def test_starting_position(self):
        world.load_tiles()
        print(world.tile_exists(2, 4))
        self.assertEqual(world.tile_exists(2, 4), rooms.StartingRoom)
