# class named board which represents quoridor board
# tracking position of pieces and walls
# suggesting valid moves and wall placements 

import pygame
from .constants import BROWN, ROWS, COLS, ORANGE, SQUARE_SIZE, WIDTH, HEIGHT, BLACK, SPACE_SIZE, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.wall = []
        self.selected_piece = None
        self.create_board()
        #self.white_left = self.black_left = 1 ==> might have to remove this as there will always be 2 moving pieces on the board
    
    def draw_squares(self, win):
        Board_width = (SQUARE_SIZE*9 + SPACE_SIZE*8)
        rect_x = (WIDTH-Board_width)//2
        rect_y = (HEIGHT-Board_width)//2

        for row in range(ROWS):
            for col in range(COLS):
                #if row%2==0 and col%2==0:
                x = rect_x+col*(SQUARE_SIZE+SPACE_SIZE)
                y = rect_y+row*(SQUARE_SIZE+SPACE_SIZE)
                pygame.draw.rect(win, ORANGE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                if row < ROWS and col< COLS-1:
                    x2 = rect_x+SQUARE_SIZE+col*(SQUARE_SIZE+SPACE_SIZE)
                    y2 = rect_y+row*(SQUARE_SIZE+SPACE_SIZE)
                    pygame.draw.rect(win, BROWN, (x2, y2, SPACE_SIZE, SQUARE_SIZE))
                if row < ROWS-1 and col< COLS:
                    x3 = rect_x+col*(SQUARE_SIZE+SPACE_SIZE)
                    y3 = rect_y+SQUARE_SIZE+row*(SQUARE_SIZE+SPACE_SIZE)
                    pygame.draw.rect(win, BROWN, (x3, y3, SQUARE_SIZE, SPACE_SIZE))

                if row < ROWS-1 and col < COLS-1:
                    x1 = rect_x+SQUARE_SIZE+col*(SQUARE_SIZE+SPACE_SIZE)
                    y1 = rect_y+SQUARE_SIZE+row*(SQUARE_SIZE+SPACE_SIZE)
                    pygame.draw.rect(win, BROWN, (x1, y1, SPACE_SIZE, SPACE_SIZE))
                    



    def create_board(self):
        for row in range (ROWS):
            self.board.append([])
            for col in range (COLS):
                if col==4 and row==0:
                    self.board[row].append(Piece(row, col, WHITE))
                    
                elif col==4 and row==8:
                    self.board[row].append(Piece(row, col, BLACK))
                else:
                    self.board[row].append(0)


    def draw(self, win):
        self.draw_squares(win)
        for row in range (ROWS):
            for col in range (COLS):
                piece = self.board[row][col]
                if piece!=0:
                    piece.draw(win)
                    