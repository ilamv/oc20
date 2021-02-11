"""Draw text to the screen."""
import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
MAGENTA = (255, 0, 255)

pygame.init()
screen = pygame.display.set_mode((640, 340))

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

t0 = time.time()
font = pygame.font.SysFont(None, 48)
print('time needed for Font creation :', time.time()-t0)

img = font.render(sysfont, True, RED)
rect = img.get_rect()
pygame.draw.rect(img, BLUE, rect, 1)

font1 = pygame.font.SysFont('ILARIA LA BEST', 72)
img1 = font1.render('ILARIA LA BEST', True, MAGENTA)

font2 = pygame.font.SysFont('Amélie la + belle', 72)
img2 = font2.render('Amélie la + belle', True, BLUE)

font3 = pygame.font.SysFont('Wawa le bg', 72)
img3 = font3.render('Wawa le bg', True, GREEN)

font4 = pygame.font.SysFont('Paulsen + Thalia = <3 ', 72)
img4 = font4.render('Paulsen + Thalia = <3', True, RED)

fonts = pygame.font.get_fonts()
print(len(fonts))
for i in range(7):
    print(fonts[i])

running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(background)
    #screen.blit(img, (20, 20))
    screen.blit(img1, (20, 50))
    screen.blit(img2, (20, 120))
    screen.blit(img3, (20, 190))
    screen.blit(img4, (20, 260))
    pygame.display.update()

pygame.quit()