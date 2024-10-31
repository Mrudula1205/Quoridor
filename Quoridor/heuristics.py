from .constants import WHITE, BLACK, ROWS, COLS, WIDTH, HEIGHT
from .piece import Piece
import pygame
win = pygame.display.set_mode(( WIDTH, HEIGHT ))

def evaluate(board):
    score = 0

    # Distance to Goal
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE:  # AI
                    score -= (ROWS - piece.row)
                elif piece.color == BLACK:  # Human player
                    score += (piece.row)

    # Wall Obstruction (penalize based on walls blocking direct paths)
    for row in range(ROWS):
        for col in range(COLS):
            if isinstance(board.board[row][col], Piece):
                piece = board.board[row][col]
                if board.is_wall(piece, piece.row - 2, piece.col):  # Example check for walls
                    if piece.color == WHITE:
                        score += 3  # Penalize if a wall is blocking the AI
                    elif piece.color == BLACK:
                        score -=8  # Penalize if a wall is blocking the human player
    # Piece Mobility
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE:  # AI
                    score -= len(get_valid_moves(board, piece))
                elif piece.color == BLACK:  # Human player
                    score += len(get_valid_moves(board, piece))

    return score

'''def evaluate(board):
    score = 0
    # Distance to Goal
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE:  # AI
                    score -= 2 * (ROWS - piece.row)
                elif piece.color == BLACK:  # Human player
                    score += piece.row

    # Wall Obstruction (penalize based on walls blocking direct paths)
    for row in range(ROWS):
        for col in range(COLS):
            if isinstance(board.board[row][col], Piece):
                piece = board.board[row][col]
                if board.is_wall(piece, piece.row - 1, piece.col):
                    if piece.color == WHITE:
                        score += 1  # Penalize more if a wall is blocking the AI
                    elif piece.color == BLACK:
                        score -= 20  # Penalize heavily if a wall is blocking the human player

    # Piece Mobility (additional layer to incentivize wall placement)
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE:  # AI
                    score -= 2 * len(get_valid_moves(board, piece))
                elif piece.color == BLACK:  # Human player
                    score += 2 * len(get_valid_moves(board, piece))

    return score'''

def get_valid_moves(board, piece):
    valid_moves = []
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Standard Quoridor moves

    for direction in directions:
        new_row = piece.row + direction[0]
        new_col = piece.col + direction[1]
        if board.valid_move(piece, new_row, new_col) and not board.is_wall(piece, new_row, new_col):
            valid_moves.append((piece, new_row, new_col))

    return valid_moves

def draw_text(win, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    win.blit(text_surface, text_rect)

def game_over(board):
    for row in board.board:
        for piece in row:
            if piece != 0:
                if piece.color == WHITE and piece.row == 0:  # AI reaches the top row
                    print("White wins") 
                    draw_text(win, "White wins", 64, (128, 128, 0), WIDTH // 2, HEIGHT // 2)
                    pygame.display.update()
                    pygame.time.wait(10000)
                    return True
                elif piece.color == BLACK and piece.row == ROWS - 1:  # Human reaches the bottom row
                    print("Black wins")
                    draw_text(win, "Black wins", 64, (128, 128, 0), WIDTH // 2, HEIGHT // 2)
                    pygame.display.update()
                    pygame.time.wait(10000)
                    return True
    #print('game over!!')
    return False