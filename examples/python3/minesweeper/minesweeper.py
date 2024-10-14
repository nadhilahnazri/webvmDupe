from board import Board


class Minesweeper:
    """A class to represent a minesweeper game."""

    def __init__(self):
        """Initialize class attributes."""
        self.round = 1
        self.round_won = 0
        self.round_lost = 0

    @staticmethod
    def user_input():
        """Requesting user input and validating choice."""
        while True:
            # Display user input options.
            print("\nSelect your difficulty.")
            print("\nBeginner: Type '1'")
            print("Intermediate: Type '2'")
            print("Expert: Type '3'")

            # Requesting user input.
            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2, 3]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return 10, 10
            elif user_input == 2:
                return 16, 40
            elif user_input == 3:
                return 30, 99

    @staticmethod
    def user_input_row():
        """Requesting user input and validating number."""
        while True:
            # Requesting user input.
            try:
                user_input = int(input("\nSelect row: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            if user_input < 0:
                print("\nThat is a negative number.")
            else:
                return user_input

    @staticmethod
    def user_input_column():
        """Requesting user input and validating number."""
        while True:
            # Requesting user input.
            try:
                user_input = int(input("\nSelect column: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            if user_input < 0:
                print("\nThat is a negative number.")
            else:
                return user_input

    def add_round(self):
        """Add point to round played."""
        self.round += 1

    def add_round_won(self):
        """Add point to round won."""
        self.round_won += 1

    def add_round_lost(self):
        """Add point to round lost."""
        self.round_lost += 1

    def scoreboard(self):
        """Display the rounds played/won/lost."""
        print(
            f"\nROUND: {self.round} | WON: {self.round_won} | LOST: {self.round_lost}"
        )

    def game(self, dimension_size, number_bombs):
        """Start game with dimension size and number of bombs."""
        # Creating the board.
        board = Board(dimension_size, number_bombs)
        safe = True

        while len(board.dug) < board.dimension_size**2 - number_bombs:
            print()
            print(board)
            print("\nWhere would you like to dig?")

            # Requesting user input.
            row = self.user_input_row()
            column = self.user_input_column()

            if (
                row < 0
                or row >= board.dimension_size
                or column < 0
                or column >= dimension_size
            ):
                print("\nInvalid location. Please try again.")
                continue

            # Verifying a valid dig.
            safe = board.dig(row, column)
            if not safe:
                break

        # Win conditions.
        if safe:
            print()
            board.dug = [
                (r, c)
                for r in range(board.dimension_size)
                for c in range(board.dimension_size)
            ]
            print(board)
            print("\nWINNER!")
            self.add_round_won()
        else:
            print()
            board.dug = [
                (r, c)
                for r in range(board.dimension_size)
                for c in range(board.dimension_size)
            ]
            print(board)
            print("\nGAME OVER!")
            self.add_round_lost()

    def start_game(self):
        """Starting the minesweeper game."""
        # Requesting user input.
        user_input = self.user_input()
        # Assign user input to appropriate difficulty.
        size, bombs = user_input

        while True:
            # Display scoreboard.
            self.scoreboard()
            # Assign appropriate size and bombs.
            self.game(size, bombs)
            self.add_round()
            # Requesting user input.
            self.restart()

            continue

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            # Display user input options.
            print("\nPlay Again?")
            print("\nYes: Type '1'")
            print("No: Type '2'")

            # Requesting user input.
            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return
            elif user_input == 2:
                quit("\nThank you for playing!")
