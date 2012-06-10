"""Python terminal board"""

class TextBoard(object):
    """To be  used for debugging and early development mainly."""
    def __init__(self, boatlist=None, size_x=4, size_y=4):
        """
        Will init a board of size_x * size_y

        @param boatlist: The list of boats to be displayed on board
        @type boatlist: Python list object

        @param boardsize: The size of the game board, where boardsize[0]
        is x and boardsize[1] = y
        @type boatlist: Python list object containing ints

        """
        self._boats = boatlist

        self._board = []
        self._board_col = []
        count = 0
        for row in range(size_y):
            for col in range(size_x):
                self._board_col.append(self._padded(count))
                count += 1

            self._board.append(self._board_col)
            self._board_col = []

        if boatlist:
            self.add_boats(self._boats)

    @property
    def board(self):
        return self._board

    def clear_board(self):
        for row in range(size_y):
            for col in range(size_x):
                self._board_col.append(self._padded(count))
                count += 1

            self._board.append(self._board_col)
            self._board_col = []

    def add_boats(self, boats):
        """Add all boats from list boats to game board."""
        for boat in boats:
            x = boat.x
            y = boat.y
            self.board[y][x] = boat.name

    def _padded(self, num):
        return "~~"
        if num < 10:
            return '0' + str(num)
        else:
            return str(num)

    def update_board(self):
        self.clear_board()
        self.add_boats(self._boats)

    def print_board(self):
        for cell in self.board:
            print cell


    def __str__(self):
        s = []
        for row in self.board:
            s.append(str(row))
        return "\n".join(s)





from boat import Boat
empty_board = TextBoard(None)
empty_board.print_board()

boats = []
boats.append(Boat(name='me'))
boats.append(Boat(x=3, y=3, name="b2"))
boats.append(Boat(x=2, y=1, name="b3"))

#~ boats = [boat1, boat2, boat3]
print "\n\nPopulated board"
board = TextBoard(boats)
print board

move = raw_input("\[left:right:up:down\] --> ")
boats[0].move(move)
board.update_board()
print board
