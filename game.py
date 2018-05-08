import pygame
from pygame.locals import *
pygame.init()

#Ouverture fenetre PyGame
windows = pygame.display.set_mode((520, 160))
#chargement du fond
fond = pygame.image.load("structures.png")
windows.blit(fond, (0,0))
#chargement MacGiver
MacGyver = pygame.image.load("MacGyver.png").convert_alpha()
position_perso = perso.get_rect()
windows.blit(MacGyver, (0,0))
#chargement Gardien
Gardien = pygame.image.load("Gardien.png").convert_alpha()
windows.blit(Gardien, (0,0))
#rafraichissement ecran
pygame.display.flip()

continuer = 1

while continuer:


	for event in pygame.event.get():

		if event.type == QUIT:
			continuer = 0

        if event.type == KEYDOWN:
        	if event.key == K_LEFT:
        		position_perso = position_perso.move(-50,0)
        	if event.key == K_RIGHT:
        		position_perso = position_perso.move(50,0)
        	if event.key == K_UP:
        		position_perso = position_perso.move(0,-50)
        	if event.key == K_DOWN:
        		position_perso = position_perso.move(0,50)


#autre fonction:
