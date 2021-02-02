import pygame
from pygame.locals import *

#Tools > Install packages...
#Find pygame
#Install

#défini des couleurs
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
CYAN = (0.255,255)
MAGENTA = (255,0,255)

#défini l'écran
background = GRAY

key_dict = {K_k:BLACK, K_r:RED, K_b: BLUE, K_y:YELLOW}

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen.fill(GRAY)
pygame.display.update()
#taille de base (640,480)
#créé un écran de couleur grise

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# ça sert à pouvoir avoir l'icone rouge afin de fermer la fenêtre

            
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key in key_dict:
                background = key_dict[event.key]
#             print(event)
#             if event.key == pygame.K_r:
#                 background = RED
#             elif event.key == pygame.K_g:
#                 background = GREEN
                
            screen.fill(background)
            pygame.display.update()
# ça sert à changer la couleur du fond avec la touche (r) --> rouge et avec la touche (g) --> vert 
        
pygame.quit()