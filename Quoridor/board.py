# class named board which represents quoridor board
# tracking position of pieces and walls
# suggesting valid moves and wall placements 

import pygame
from .constants import BROWN, ROWS, COLS, ORANGE, SQUARE_SIZE, WIDTH, HEIGHT, BLACK, SPACE_SIZE, WHITE, GREY
from .piece import Piece
from .wall import Wall, is_valid_wall
from .piece_status import BoardPieceStatus

class Board:
    def __init__(self, player1_row, player1_col, player2_row, player2_col):
        self.board = []
        self.walls = []
        self.selected_piece = None
        self.create_board(player1_row, player1_col, player2_row, player2_col)
        #self.white_left = self.black_left = 1 ==> might have to remove this as there will always be 2 moving pieces on the board
    
    def draw_squares(self, win):
        Board_width = (SQUARE_SIZE*9 + SPACE_SIZE*8)
        rect_x = (WIDTH-Board_width)//2
        rect_y = (HEIGHT-Board_width)//2

        for row in range(ROWS):
            for col in range(COLS):
                if row % 2 == 0 and col % 2 == 0:  # Squares for pawns
                    x = rect_x + (col // 2) * (SQUARE_SIZE + SPACE_SIZE)
                    y = rect_y + (row // 2) * (SQUARE_SIZE + SPACE_SIZE)
                    pygame.draw.rect(win, ORANGE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                
                elif row % 2 == 0 and col % 2 == 1:  # Horizontal spaces for walls
                    x = rect_x + ((col - 1) // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    y = rect_y + (row // 2) * (SQUARE_SIZE + SPACE_SIZE)
                    pygame.draw.rect(win, BROWN, (x, y, SPACE_SIZE, SQUARE_SIZE))
                elif row % 2 == 1 and col % 2 == 0:  # Vertical spaces for walls
                    x = rect_x + (col // 2) * (SQUARE_SIZE + SPACE_SIZE)
                    y = rect_y + ((row - 1) // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    pygame.draw.rect(win, BROWN, (x, y, SQUARE_SIZE, SPACE_SIZE))
                elif row % 2 == 1 and col % 2 == 1:  # Intersection points for walls
                    x = rect_x + ((col - 1) // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    y = rect_y + ((row - 1) // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    pygame.draw.rect(win, BROWN, (x, y, SPACE_SIZE, SPACE_SIZE))
        for wall in self.walls:
            for pos in wall.affected_positions():
                row, col = pos
                if (row%2==1 and col%2==1):
                    x = rect_x + (col // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    y = rect_y + (row // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    pygame.draw.rect(win, GREY, (x, y, SPACE_SIZE, SPACE_SIZE))
                if wall.orientation == 'horizontal':
                    x = rect_x + (col // 2) * (SQUARE_SIZE + SPACE_SIZE)
                    y = rect_y + (row // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    pygame.draw.rect(win, GREY, (x, y, SQUARE_SIZE, SPACE_SIZE))
                    
                elif wall.orientation == 'vertical':
                    x = rect_x + (col // 2) * (SQUARE_SIZE + SPACE_SIZE) + SQUARE_SIZE
                    y = rect_y + (row // 2) * (SQUARE_SIZE + SPACE_SIZE)
                    pygame.draw.rect(win, GREY, (x, y, SPACE_SIZE, SQUARE_SIZE))

    

                    

    def create_board(self, player1_row, player1_col, player2_row, player2_col):
        for row in range (ROWS):
            self.board.append([])
            for col in range (COLS):
                if col==player1_col and row==player1_row:
                    player = Piece(row, col, WHITE)
                    self.board[row].append(player)
                    
                elif col==player2_col and row==player2_row:
                    ai = Piece(row, col, BLACK)
                    self.board[row].append(ai)
                else:
                    self.board[row].append(0)

    def get_piece(self, color):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece.color == color:
                    return piece
        return None
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range (ROWS):
            for col in range (COLS):
                piece = self.board[row][col]
                if piece!=0:
                    piece.draw(win)
    
    def add_wall(self, row, col, orientation):
        wall = Wall(row, col, orientation)
        if is_valid_wall(self, wall):
            self.walls.append(wall)
            print(f"Wall placed at ({row}, {col}) in {orientation} orientation.")
            return True
        else:
            print("Invalid wall placement.")
            return False
        
    '''def valid_move():
        pass

    def move_piece():
        pass

    def get_piece(self):
        for row in range (ROWS):
            for col in range (COLS):
                if self.board[row][col] == WHITE:
                    return row, col'''
