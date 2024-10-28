from .constants import WHITE, BLACK, ROWS, COLS
from .piece import Piece
def evaluate(board):
    score = 0

    # Distance to Goal
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE:  # AI
                    score -= 2*(ROWS - piece.row)
                elif piece.color == BLACK:  # Human player
                    score += piece.row

    # Wall Obstruction (penalize based on walls blocking direct paths)
    for row in range(ROWS):
        for col in range(COLS):
            if isinstance(board.board[row][col], Piece):
                piece = board.board[row][col]
                if board.is_wall(piece, piece.row - 2, piece.col):  # Example check for walls
                    if piece.color == WHITE:
                        score += 1  # Penalize if a wall is blocking the AI
                    elif piece.color == BLACK:
                        score -= 1  # Penalize if a wall is blocking the human player'''
    # Piece Mobility
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE:  # AI
                    score -= len(get_valid_moves(board, piece))+5
                elif piece.color == BLACK:  # Human player
                    score += len(get_valid_moves(board, piece))+5

    return score

def get_valid_moves(board, piece):
    valid_moves = []
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Standard Quoridor moves

    for direction in directions:
        new_row = piece.row + direction[0]
        new_col = piece.col + direction[1]
        if board.valid_move(piece, new_row, new_col) and not board.is_wall(piece, new_row, new_col):
            valid_moves.append((piece, new_row, new_col))

    return valid_moves

def game_over(board):
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE and piece.row == 0:  # AI reaches the top row
                    return True
                elif piece.color == BLACK and piece.row == ROWS - 1:  # Human reaches the bottom row
                    return True
    return False
