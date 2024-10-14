import pygame
from Quoridor.constants import WIDTH, HEIGHT, SQUARE_SIZE, SPACE_SIZE
from Quoridor.board import Board
FPS = 60
WIN = pygame.display.set_mode(( WIDTH, HEIGHT ))

Board_width = (SQUARE_SIZE*9 + SPACE_SIZE*8)
rect_x = (WIDTH-Board_width)//2
rect_y = (HEIGHT-Board_width)//2

def get_mouse_position():
    x, y = pygame.mouse.get_pos()
    if (x>=rect_x and y>=rect_y and x<=Board_width+rect_x and y<=Board_width+rect_y):
        col = ((x - rect_x) // (SQUARE_SIZE + SPACE_SIZE)) * 2
        row = ((y - rect_y) // (SQUARE_SIZE + SPACE_SIZE)) * 2
        # Correct for clicking within the space
        if (x - rect_x) % (SQUARE_SIZE + SPACE_SIZE) >= SQUARE_SIZE:
            col += 1
        if (y - rect_y) % (SQUARE_SIZE + SPACE_SIZE) >= SQUARE_SIZE:
            row += 1
    return row, col, x, y

def get_piece(row, col):
    return Board.board[row][col]

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    mode = 'move'
    selected_piece = None
    

    while run:
        clock.tick(FPS)
        pass
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  # Press 'M' to toggle mode
                    if mode == 'move':
                        mode = 'wall'
                    else:
                        mode = 'move'
                    print(f"Mode switched to {mode}")
            if event.type == pygame.MOUSEBUTTONDOWN: #when a player click on the screen we check for turn and further decision
                row, col, x, y = get_mouse_position()
                if mode == 'wall':
                    if event.button == 1:  # Left click for horizontal
                        if row % 2 == 1 and col % 2 == 0:  # Ensure it's a valid horizontal space
                            print(row, col)
                            board.add_wall(row, col, 'horizontal')
                    elif event.button == 3:  # Right click for vertical
                        if row % 2 == 0 and col % 2 == 1:  # Ensure it's a valid vertical space
                            print(row, col, "vertical")
                            board.add_wall(row, col, 'vertical')
                elif mode == 'move':
                    pass
                    '''if selected_piece:
                        board.move_piece(selected_piece, row, col)
                        selected_piece = None
                    else:
                        selected_piece = board.get_piece()'''
            '''if event.type == pygame.KEYDOWN and selected_piece and mode == 'move':
                new_row, new_col = selected_piece.row, selected_piece.col
                if event.key == pygame.K_LEFT:
                    new_col -= 1
                elif event.key == pygame.K_RIGHT:
                    new_col += 1
                elif event.key == pygame.K_UP:
                    new_row -= 1
                elif event.key == pygame.K_DOWN:
                    new_row += 1

                if board.valid_move(selected_piece, new_row, new_col):
                    board.move_piece(selected_piece, new_row, new_col)
            # Space for drag and drop feature too'''
        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()