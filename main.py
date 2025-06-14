import pygame
from game.board import Board
from ui.renderer import Renderer

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Fusion Chess")
clock = pygame.time.Clock()

board = Board()
renderer = Renderer(screen, board, pygame)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    renderer.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
