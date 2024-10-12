import pygame
from Quoridor.constants import WIDTH, HEIGHT
from Quoridor.board import Board
FPS = 60
WIN = pygame.display.set_mode(( WIDTH, HEIGHT ))

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        pass
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #when a player click on the screen we check for turn and further decision
                pass
            # Space for drag and drop feature too
        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()