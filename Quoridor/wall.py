class Wall:
    def __init__(self, row, col, orientation):
        self.row = row
        self.col = col
        self.orientation = orientation

    def affected_positions(self):
        positions = []
        if self.orientation == 'horizontal':
            positions.append((self.row, self.col))
            positions.append((self.row, self.col+1))
            positions.append((self.row, self.col+2))
        elif self.orientation == 'vertical':
            positions.append((self.row, self.col))
            positions.append((self.row+1, self.col))
            positions.append((self.row+2, self.col))
        
        return positions

def is_valid_wall(board, wall):
    for pos in wall.affected_positions():
        row, col = pos
        if row >= len(board.board) or col >= len(board.board[0]):
            return False
    for existing_wall in board.walls:
        for pos in wall.affected_positions():
            if pos in existing_wall.affected_positions():
                return False
    return True

