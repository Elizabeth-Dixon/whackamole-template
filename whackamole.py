import pygame, sys
import random

from pygame import MOUSEBUTTONDOWN

pygame.init()
screen = pygame.display.set_mode((640, 512))
game_over = False


#pygame.MOUSEBUTTONDOWN(event.pos)


'''

def draw_grid():
        #draw horizontal lines
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )
        #draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH
            )


'''





'''
board = []
for row in range(board_height):
    board.append([])
    for col in range(board_width):
        board[row].append(0)

'''
col = 0
row = 0



def main():
    screen = pygame.display.set_mode((20, 16))

for event in pygame.event.get():

   # blah

    try:

        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")


        clock = pygame.time.Clock()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    row = random.randrange(0,20)*32
                    col = random.randrange(0,16)*32
                    screen.blit(mole_image, (col, row))
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(row, col)))
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "dark green", (i, 0), (i, 512))
            for i in range(0,512,32):
                pygame.draw.line(screen, "dark green", (0, i), (640, i))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()
if __name__ == "__main__":
    main()




