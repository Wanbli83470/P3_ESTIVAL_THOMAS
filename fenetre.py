#! /usr/bin/env python3
# coding: utf-8

"""Modul Random for generate the position of object"""
import random
import pygame
from pygame.locals import *
from constantes import *
from aleatoire import*

pygame.init()
""" init counter """
COUNTER = 0
"""init counter of life"""
LIFE = 1

"""Opening PyGame windows"""
windows = pygame.display.set_mode((SIZE_WINDOWS, SIZE_WINDOWS))

"""name windows"""
pygame.display.set_caption(TITLE_WINDOWS)

"""loading MacGyver"""
MacGyver = pygame.image.load(SCREEN_MACGYVER).convert_alpha()
LOCATION_HERO = MacGyver.get_rect()
windows.blit(MacGyver, LOCATION_HERO)
LOCATION_HERO.x = (MG_x)
LOCATION_HERO.y = (MG_y)

"""loading Gardien"""
GUARDIAN = pygame.image.load(SCREEN_GARDUIAN).convert_alpha()
windows.blit(GUARDIAN, (Gardien_conversion))

"""loading ether"""
ether = pygame.image.load(SCREEN_ETHER).convert_alpha()
windows.blit(ether, (RANDOM_OBJECT))

"""loading NEEDLE"""
NEEDLE = pygame.image.load(SCREEN_NEEDLE).convert_alpha()
windows.blit(NEEDLE, (RANDOM_OBJECT2))

"""loading COMPASS"""
COMPASS = pygame.image.load(SCREEN_COMPASS).convert_alpha()
windows.blit(COMPASS, (RANDOM_OBJECT3))

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

windows.blit(LOCATION_TEXT, (20, 715))

"""loading arrivée"""
CORRIDOR = pygame.image.load(SCREEN_CORRIDOR).convert()
windows.blit(CORRIDOR, (0, 0))

"""loading wall"""
mur = pygame.image.load(WALL).convert()
windows.blit(mur, (0, 0))

"""loading DANGEROUS SPRITE"""
danger = pygame.image.load(SCREEN_DANGEROUS).convert()
windows.blit(danger, (0, 0))

"""loading parcours"""
CORRIDOR2 = pygame.image.load(SCREEN_ARRIVAL).convert()
windows.blit(CORRIDOR, (0, 0))

pygame.display.flip()

CONTINUE = 1

while CONTINUE == 1:

    for event in pygame.event.get():

        if event.type == QUIT:
            CONTINUE = 0

        if event.type == KEYDOWN:
            
            if event.key == K_LEFT:
                if position_x > 0:
                    if valeur_suivante_gauche in coor:
                        LOCATION_HERO = LOCATION_HERO.move(-50, 0)
            elif event.key == K_RIGHT:
                if position_x < 700:
                    if valeur_suivante_droite in coor:
                        LOCATION_HERO = LOCATION_HERO.move(50, 0)
            elif event.key == K_UP:
                if position_y > 0:
                    if valeur_suivante_haut in coor:
                        LOCATION_HERO = LOCATION_HERO.move(0, -50)
            elif event.key == K_DOWN:
                if position_y < 700:
                    if valeur_suivante_bas in coor:
                        LOCATION_HERO = LOCATION_HERO.move(0, 50)

    LOCATION_HERO_LIST = list(LOCATION_HERO)
    position_precise = LOCATION_HERO_LIST[0:2]
    position_x = position_precise[0]
    position_y = position_precise[1]

    x50 = (position_precise[0]+50)
    x_moins50 = (position_precise[0]-50)

    y50 = (position_precise[1]+50)
    y_moins50 = (position_precise[1]-50)

    valeur_suivante_droite = [x50, position_y]
    valeur_suivante_gauche = [x_moins50, position_y]
    valeur_suivante_haut = [position_x, y_moins50]
    valeur_suivante_bas = [position_x, y50]

    ROAD = "n.txt"

    ouverture = open(ROAD, 'r')
    SQUARE_X = 0
    SQUARE_Y = 0

    case = [SQUARE_X, SQUARE_Y]

    x = SQUARE_X * 50
    y = SQUARE_Y * 50

    xy = [x, y]

    LOCATION_STARTING = []
    position_arrivee = []
    coor = []
    LOCATION_WALL = []
    coor_danger = []

    for ligne in ouverture.read():
        x = SQUARE_X * 50
        y = SQUARE_Y * 50

        SQUARE_X = SQUARE_X + 1

        if SQUARE_X > 15:
            SQUARE_X = 0
            SQUARE_Y = SQUARE_Y + 1

        case = [SQUARE_X, SQUARE_Y]
        xy = [x, y]

        if ligne == "d":
            LOCATION_STARTING.append(case)
            windows.blit(CORRIDOR, (x, y))
        elif ligne == "a":
            position_arrivee.append(xy)
            windows.blit(CORRIDOR, (x, y))
            windows.blit(GUARDIAN, (x, y))
            coor.append(xy)
        elif ligne == "o":
            coor.append(xy)
            windows.blit(CORRIDOR2, (x, y))
        elif ligne == "m":
            LOCATION_WALL.append(xy)
            windows.blit(mur, (x, y))
        elif ligne == "c":
            coor.append(xy)
            LOCATION_WALL.append(xy)
            windows.blit(danger, (x, y))

    """"condition and position for victory"""

    if position_precise == RANDOM_OBJECT:
        RANDOM_OBJECT = (750, 750)
        COUNTER += 1
        LOCATION_TEXT = font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
        rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()

    elif position_precise == RANDOM_OBJECT2:
        RANDOM_OBJECT2 = (750, 750)
        COUNTER += 1
        LOCATION_TEXT = font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
        rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()

    elif position_precise == RANDOM_OBJECT3:
        RANDOM_OBJECT3 = (750, 750)
        COUNTER += 1
        LOCATION_TEXT = font.render("Object stack : " + str(COUNTER), True, (255, 255, 255))
        rect_LOCATION_TEXT = LOCATION_TEXT.get_rect()

    if position_precise in LOCATION_WALL:
        if LIFE > 0:
            LIFE -= 4
            LOCATION_TEXT2 = font.render("LIFE : " + str(LIFE), True, (255, 255, 255))

    if LIFE <= 0:
        LOCATION_OVER = (0, 0)
        CONTINUE = 0

    if COUNTER == 3:
        MacGyver = pygame.image.load(SCREEN_MACGYVER_OBJECT).convert_alpha()

    if position_precise == Gardien_conversion and COUNTER < 3:
        LOCATION_OVER = (0, 0)
        CONTINUE = 0

    if position_precise == Gardien_conversion and COUNTER == 3:
        LOCATION_WIN = (0, 0)

    """"Refresh"""

    windows.blit(LOCATION_TEXT, (20, 715))
    windows.blit(LOCATION_TEXT2, (550, 715))
    windows.blit(MacGyver, LOCATION_HERO)
    windows.blit(NEEDLE, (RANDOM_OBJECT2))
    windows.blit(COMPASS, (RANDOM_OBJECT3))
    windows.blit(ether, (RANDOM_OBJECT))
    windows.blit(over, (LOCATION_OVER))
    windows.blit(win, (LOCATION_WIN))
    pygame.display.flip()
