```python
class Position:
def init(self, row, col):
self.row = row
self.col = col

def __repr__(self):
    return f"{self.row} {self.col}"
class Board:
def init(self, size=10):
self.size = size
self.board = [['.' for _ in range(size)] for _ in range(size)]
self.pieces = Position(0, 0)
self.turn = 1

def __str__(self):
    header ='  '
    for i in range(self.size):
        header += f' {i}'
    s = f'{header}\n'
    for row in self.board:
        s += f'{row.join(" ")} '
    return s

def __move__(self, direction):
    if self.turn == 1:
        piece = self.pieces
    else:
        piece = self.pieces[0]

    row, col = piece.row, piece.col
    if direction == 'up':
        piece.row, col = row - 1, col
        if row < 0:
            piece.row, col = row + self.size - 1, col
    elif direction == 'down':
        piece.row, col = row + 1, col
        if row >= self.size:
            piece.row, col = row - self.size, col
    elif direction == 'left':
        piece.col, row = col - 1, row
        if col < 0:
            piece.col, row = col + self.size - 1, row
    elif direction == 'right':
        piece.col, row = col + 1, row
        if col >= self.size:
            piece.col, row = col - self.size, row
    self.board[row][col] = '1'
    self.board[row][col] = '1'
    self