from .constants import BLACK, WHITE, GREY, SQUARE_SIZE, SPACE_SIZE, WIDTH, HEIGHT, ROWS, COLS
import pygame

class Piece:

    PADDING = 10
    OUTLINE = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        if self.color == BLACK: #Human - player1
            self.direction = -1
        if self.color == WHITE: #AI - player2
            self.direction = 1
            

        self.x = 0
        self.y = 0
        self.calc_path()


    def calc_path(self):
        Board_width = (SQUARE_SIZE*9 + SPACE_SIZE*8)
        rect_x = (WIDTH-Board_width)//2
        rect_y = (HEIGHT-Board_width)//2
        self.x = rect_x+(self.col // 2) * (SQUARE_SIZE + SPACE_SIZE)+SQUARE_SIZE/2
        self.y = rect_y+(self.row // 2) * (SQUARE_SIZE + SPACE_SIZE)+SQUARE_SIZE/2
        

    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

   


    def __repr__(self):
        return str(self.color)
