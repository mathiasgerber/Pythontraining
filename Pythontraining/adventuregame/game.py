from adventuregame import world
from adventuregame.player import Player


def play():
    """ The main function in which the game is looped.

    The game is looped as long as the player is still alive and did not
    achieve victory.
    """
    world.load_tiles()
    player = Player()

    # These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.entry_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)

        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            make_action(player, room)


def make_action(player, room):
    """ User input is taken to do the action the user chose. """
    print("Choose an action:\n")
    available_actions = room.available_actions()
    for action in available_actions:
        print(action)

    # Validation loop that takes the input and checks if there's a matching
    # action. If not it asks again.
    action_validator = False
    while not action_validator:
        action_input = input('Action: ')
        for action in available_actions:
            if action_input == action.hotkey:
                player.do_action(action, **action.kwargs)
                action_validator = True
                break
        else:
            print("This is not a valid action.")


if __name__ == "__main__":
    play()
