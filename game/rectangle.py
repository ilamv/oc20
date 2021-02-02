import pygame
from pygame.locals import *

width = 640
height = 420

size = width, height
GREEN = (150, 255, 150)
RED = (255, 0, 0)
GRAY = (127,127,127)
background = GRAY

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(background)

pygame.draw.rect(screen, RED, (50, 20, 220, 100))
pygame.draw.rect(screen, GREEN, (100, 150, 220, 100))

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()