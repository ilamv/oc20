import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)
path = 'bird.png'

img = pygame.image.load('bird.png')
img.convert()

img = pygame.image.load(path)
img.convert()

img0 = pygame.image.load(path)
img0.convert()

rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)

rect = img.get_rect()
rect.center = 250, 250
moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
            
        elif event.type == MOUSEBUTTONUP:
            moving = False
            
        elif event.type == MOUSEMOTION and moving:
                rect.move_ip(event.rel)

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(img, rect)
    pygame.display.flip()

pygame.quit()