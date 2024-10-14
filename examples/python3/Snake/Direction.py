import curses

class Direction:
    """This class represents directions on a plane."""

    # Using curses key codes for arrow keys
    UP = curses.KEY_UP
    LEFT = curses.KEY_LEFT
    DOWN = curses.KEY_DOWN
    RIGHT = curses.KEY_RIGHT

    # List of all directions
    DIRECTIONS = [UP, LEFT, DOWN, RIGHT]

    @staticmethod
    def opposite(direction):
        """Return the opposite of the current direction."""
        if direction == Direction.UP:
            return Direction.DOWN
        elif direction == Direction.LEFT:
            return Direction.RIGHT
        elif direction == Direction.DOWN:
            return Direction.UP
        elif direction == Direction.RIGHT:
            return Direction.LEFT
