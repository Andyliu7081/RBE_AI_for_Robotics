class ConnectFour:

    def __init__(self, board, w, h):
        """Class constructor"""
        # Board data
        self.board = board
        # Board width
        self.w = w
        # Board height
        self.h = h

    def isLineAt(self, x, y, dx, dy):
        """Return True if a line of identical tokens exists starting at (x,y)
           in direction (dx,dy)"""
        # Your code here
        if x < 0 or y < 0 or x >= self.w or y >= self.h or self.board[y][x] == 0:
            return False
        
        # Check for four in a line
        token = self.board[y][x]
        for i in range(1, 4):
            if x + dx * i < 0 or y + dy * i < 0 or x + dx * i >= self.w or y + dy * i >= self.h:
                return False
            if self.board[y + dy * i][x + dx * i] != token:
                return False
        return True

    def isAnyLineAt(self, x, y):
        """Return True if a line of identical symbols exists starting at (x,y)
           in any direction"""
        return (self.isLineAt(x, y, 1, 0) or # Horizontal
                self.isLineAt(x, y, 0, 1) or # Vertical
                self.isLineAt(x, y, 1, 1) or # Diagonal up
                self.isLineAt(x, y, 1, -1)) # Diagonal down

    def getOutcome(self):
        """Returns the winner of the game: 1 for Player 1, 2 for Player 2, and
           0 for no winner"""
        # Your code here, use isAnyLineAt()
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] != 0 and self.isAnyLineAt(x, y):
                    return self.board[y][x]
        return 0

    def printOutcome(self):
        """Prints the winner of the game"""
        o = self.getOutcome()
        if o == 0:
            print("No winner")
        else:
            print("Player", o, " won")


# if __name__ == "__main__":

#     W = 7
#     H = 6

#     # First board configuration
#     BOARD1 = [
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0]
#     ]
#     c = ConnectFour(BOARD1, W, H)
#     c.printOutcome()

#     # Second board configuration
#     BOARD2 = [
#         [1, 1, 1, 1, 2, 1, 0],
#         [0, 2, 2, 2, 0, 0, 0],
#         [0, 0, 2, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0]
#     ]
#     c = ConnectFour(BOARD2, W, H)
#     c.printOutcome()
