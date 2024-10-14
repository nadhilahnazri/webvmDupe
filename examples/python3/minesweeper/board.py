from random import randint


class Board:
    """A class to represent a minesweeper board."""

    def __init__(self, dimension_size, number_bombs):
        """Initialize class attributes."""
        self.dimension_size = dimension_size
        self.number_bombs = number_bombs
        self.board = self.create_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def create_new_board(self):
        """Creating a new board based on dimension size."""
        # Creating a board.
        board = [
            [None for _ in range(self.dimension_size)]
            for _ in range(self.dimension_size)
        ]

        bombs_planted = 0
        # Planting the bombs on board.
        while bombs_planted < self.number_bombs:
            location = randint(0, self.dimension_size**2 - 1)
            row = location // self.dimension_size
            column = location % self.dimension_size

            if board[row][column] == "*":
                continue

            board[row][column] = "*"
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        """Adding values to the board."""
        for r in range(self.dimension_size):
            for c in range(self.dimension_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_number_neighboring_bombs(r, c)

    def get_number_neighboring_bombs(self, row, column):
        """Verifying neighboring bombs."""
        number_neighboring_bombs = 0
        for r in range(
            max(0, row - 1), min(self.dimension_size - 1, row + 1) + 1
        ):
            for c in range(
                max(0, column - 1), min(self.dimension_size - 1, column + 1) + 1
            ):
                if r == row and c == column:
                    continue
                if self.board[r][c] == "*":
                    number_neighboring_bombs += 1
        return number_neighboring_bombs

    def dig(self, row, column):
        """Verifying a dig location."""
        self.dug.add((row, column))

        if self.board[row][column] == "*":
            return False
        elif self.board[row][column] > 0:
            return True

        for r in range(
            max(0, row - 1), min(self.dimension_size - 1, row + 1) + 1
        ):
            for c in range(
                max(0, column - 1), min(self.dimension_size - 1, column + 1) + 1
            ):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        """Return a string that shows the board."""
        visible_board = [
            [None for _ in range(self.dimension_size)]
            for _ in range(self.dimension_size)
        ]
        for r in range(self.dimension_size):
            for c in range(self.dimension_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = " "

        # Represent a string.
        string_rep = ""

        # Max column width for print output.
        widths = []
        for idx in range(self.dimension_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        # Printing the csv strings.
        indices = [i for i in range(self.dimension_size)]
        indices_row = "   "
        cells = []
        for idx, c in enumerate(indices):
            layout = "%-" + str(widths[idx]) + "s"
            cells.append(layout % c)
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            r = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, c in enumerate(r):
                layout = "%-" + str(widths[idx]) + "s"
                cells.append(layout % c)
            string_rep += " |".join(cells)
            string_rep += " |\n"

        str_len = int(len(string_rep) / self.dimension_size)
        string_rep = (
            indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len
        )
        return string_rep
