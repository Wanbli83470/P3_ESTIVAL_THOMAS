#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import*
from constantes import*
from classMG import *

pygame.init()

windows = pygame.display.set_mode((SIZE_WINDOWS, SIZE_WINDOWS))
pygame.display.flip()

""" init counter """
COUNTER = 0
"""init counter of life"""
LIFE = 1
"""name windows"""
pygame.display.set_caption(TITLE_WINDOWS)
"""MacGyver"""
MG = MacGyver()
MG.generate()
LOCATION_HERO = MG.LOCATION_HERO[0:2]
LOCATION_HERO_X = LOCATION_HERO[0]
LOCATION_HERO_Y = LOCATION_HERO[1]

"""grille du jeu"""
GRILLE = Grille()
GRILLE.parcours()
GRILLE.Random()

RANDOM_OBJECT = GRILLE.Random()

RANDOM_OBJECT2 = GRILLE.Random()

RANDOM_OBJECT3 = GRILLE.Random()

LOCATION_COULOIR = GRILLE.coor
LOCATION_GUARDIAN = GRILLE.position_arrivee
print(LOCATION_COULOIR)
print(LOCATION_GUARDIAN)

"""object1"""
object1 = ElementGrille()
object1.generate(pygame.image.load(SCREEN_ETHER).convert_alpha())
object1.random(RANDOM_OBJECT)
object1.affiche()

"""object2"""
object2 = ElementGrille()
object2.generate(pygame.image.load(SCREEN_NEEDLE).convert_alpha())
object2.random(RANDOM_OBJECT2)
object2.affiche()

"""object3"""
object3 = ElementGrille()
object3.generate(pygame.image.load(SCREEN_COMPASS).convert_alpha())
object3.random(RANDOM_OBJECT3)
object3.affiche()

"""loading Game over"""
over = pygame.image.load(SCREEN_GAMEOVER).convert_alpha()
windows.blit(over, (0, 0))
LOCATION_OVER = (750, 750)

"""loading WIN"""
win = pygame.image.load(SCREEN_WIN).convert_alpha()
windows.blit(win, (0, 0))
LOCATION_WIN = (750, 750)

"""objets ramasses"""
font=pygame.font.Font(None, 50)
LOCATION_TEXT=font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()

""""life point COUNTER"""
LIFE_POINT_ = pygame.font.Font(None, 50)
LOCATION_TEXT2=font.render("LIFE : " + str(LIFE), True, (255, 255, 255))
rect_LOCATION_TEXT2 = LOCATION_TEXT2.get_rect()

position_LOCATION_TEXTe = (750, 750)
windows.blit(LOCATION_TEXT, (20, 715))

pygame.display.flip()
CONTINUE = 0

while CONTINUE == 0:

    for event in pygame.event.get():

        if event.type == QUIT:
            CONTINUE = 1

        if event.type == KEYDOWN:

			if event.key == K_RIGHT:
				if LOCATION_HERO_X < 700:
					MG.move('droite')
			elif event.key == K_LEFT:
				if LOCATION_HERO_X > 0:
					MG.move('gauche')
			elif event.key == K_UP:
				if LOCATION_HERO_Y > 0:
					MG.move('haut')
			elif event.key == K_DOWN:
				if LOCATION_HERO_Y < 700:
					MG.move('bas')


	"""LOCATION_HERO FOR MOVE"""
	LOCATION_HERO = MG.LOCATION_HERO[0:2]
	"""LOCATION X AND Y"""
	LOCATION_HERO_X = LOCATION_HERO[0]
	LOCATION_HERO_Y = LOCATION_HERO[1]
	"""LOCATION FOR MOVE"""
	LOCATION_HERO_X50 = (LOCATION_HERO[0]+50)
	MOVE_LOCATION_HERO_X50 = LOCATION_HERO_X50,LOCATION_HERO_Y
	LOCATION_HERO_Y50 = (LOCATION_HERO[1]+50)
	LOCATION_HERO_X_50 = (LOCATION_HERO[0]-50)
	LOCATION_HERO_Y_50 = (LOCATION_HERO[1]-50)

    """"condition and position for victory"""

    if LOCATION_HERO == RANDOM_OBJECT:
		RANDOM_OBJECT = (750, 750)
		COUNTER += 1
		LOCATION_TEXT = font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
		rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()

    elif LOCATION_HERO == RANDOM_OBJECT2:
		RANDOM_OBJECT2 = (750, 750)
		COUNTER += 1
		LOCATION_TEXT = font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
		rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()

    elif LOCATION_HERO == RANDOM_OBJECT3:
		RANDOM_OBJECT3 = (750, 750)
		COUNTER += 1
		LOCATION_TEXT = font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
		rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()


    """TEST FOR LIFE"""
    if LIFE <= 0:
        LOCATION_OVER = (0, 0)
        CONTINUE = 1
    """TEST FOR VICTORY"""
    if LOCATION_HERO == LOCATION_GUARDIAN and COUNTER == 3:
        LOCATION_WIN = (0, 0)
    """TEST FOR DEFEAT"""
    if LOCATION_HERO == LOCATION_GUARDIAN and COUNTER < 3:
        LOCATION_OVER = (0, 0)
        CONTINUE = 1


    MG.affiche()
    GRILLE.parcours()
    object1.affiche()
    object1.random(RANDOM_OBJECT)
    object2.affiche()
    object2.random(RANDOM_OBJECT2)
    object3.affiche()
    object3.random(RANDOM_OBJECT3)
    MG.affiche()
    windows.blit(over, (LOCATION_OVER))
    windows.blit(win, (LOCATION_WIN))
    windows.blit(LOCATION_TEXT, (20, 715))
    windows.blit(LOCATION_TEXT2, (550, 715))
    pygame.display.flip()