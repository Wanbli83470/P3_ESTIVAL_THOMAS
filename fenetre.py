#-*- coding:utf-8 -*-
"""Modul Random for generate the position of object"""
import random
import pygame
from pygame.locals import *
from constantes import *
from aleatoire import*



pygame.init()
#couleur
#compteur
counter = 0
#vie
vie = 4
#Opening PyGame windows
windows = pygame.display.set_mode((size_windows, size_windows))
#name windows
pygame.display.set_caption(titre_fenetre)
#loading background
fond = pygame.image.load(image_fond)
windows.blit(fond, (0, 0))
#loading MacGyver
MacGyver = pygame.image.load(image_MacGyver).convert_alpha()
position_perso = MacGyver.get_rect()
windows.blit(MacGyver, position_perso)
position_perso.x = (MG_x)
position_perso.y = (MG_y)
#loading Gardien
Gardien = pygame.image.load(image_Gardien).convert_alpha()
windows.blit(Gardien, (Gardien_conversion))
#loading ether
#loading seringue
ether = pygame.image.load(image_ether).convert_alpha()
windows.blit(ether, (objet_aleatoire))
#loading aiguille
aiguille = pygame.image.load(image_aiguille).convert_alpha()
windows.blit(aiguille, (objet_aleatoire2))
#loading boussole
boussole = pygame.image.load(image_boussole).convert_alpha()
windows.blit(boussole, (RANDOM_OBJECT3))
#loading Game over
over = pygame.image.load(image_gameover).convert_alpha()
windows.blit(over, (0, 0))
position_over = (750, 750)
#loading WIN
win = pygame.image.load(image_win).convert_alpha()
windows.blit(win, (0, 0))
position_win = (750, 750)
# objets ramasses
font=pygame.font.Font(None, 50)
text=font.render("objets ramasses : " + str(counter), True, (255, 255, 255))
rect_text = text.get_rect()
#compteur point de vie
points_de_vies = pygame.font.Font(None, 50)
text2=font.render("SANTE : " + str(vie), True, (255, 255, 255))
rect_text2 = text2.get_rect()

position_texte = (750, 750)
windows.blit(text, (20, 715))

#loading arrivée
top = pygame.image.load(image_ouverture).convert()
windows.blit(top, (0, 0))
#loading wall
mur = pygame.image.load(wall).convert()
windows.blit(mur, (0, 0))
#loading case danger
danger = pygame.image.load(image_casedanger).convert()
windows.blit(danger, (0, 0))
#loading parcours
top2 = pygame.image.load(image_depart).convert()
windows.blit(top, (0, 0))

pygame.display.flip()




continuer = 1

while continuer == 1:

 
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            
            if event.key == K_LEFT:
                if position_x > 0:
                    if valeur_suivante_gauche in coor:
                        position_perso = position_perso.move(-50, 0)
            elif event.key == K_RIGHT:
                if position_x < 700:
                    if valeur_suivante_droite in coor:
                        position_perso = position_perso.move(50, 0)
            elif event.key == K_UP:
                if position_y > 0:
                    if valeur_suivante_haut in coor:
                        position_perso = position_perso.move(0, -50)
            elif event.key == K_DOWN:
                if position_y < 700:
                    if valeur_suivante_bas in coor:
                        position_perso = position_perso.move(0, 50)

 


    position_precise = (position_perso[0:2])
    position_x = position_precise[0]
    position_y = position_precise[1]

    x50=(position_precise[0]+50)
    x_moins50=(position_precise[0]-50)

    y50=(position_precise[1]+50)
    y_moins50=(position_precise[1]-50)

    valeur_suivante_droite = [x50, position_y]
    valeur_suivante_gauche = [x_moins50, position_y]
    valeur_suivante_haut = [position_x, y_moins50]
    valeur_suivante_bas = [position_x, y50]

    chemin = "n.txt"

    ouverture = open(chemin, 'r')
    case_x = 0
    case_y = 0

    case = [case_x, case_y]

    x = case_x * 50
    y = case_y * 50

    xy = [x, y]

    position_depart = []
    position_arrivee = []
    coor = []
    coor_mur = []
    coor_danger = []

    for ligne in ouverture.read():
        x = case_x * 50
        y = case_y * 50

        case_x = case_x +1

        if case_x > 15 :
            case_x = 0
            case_y = case_y + 1

        case = [case_x, case_y]
        xy = [x, y]

        if ligne == "d":
            position_depart.append(case)
            windows.blit(top, (x, y))
        elif ligne == "a":
            position_arrivee.append(xy)
            windows.blit(top, (x, y))
            windows.blit(Gardien, (x, y))
            coor.append(xy)
        elif ligne == "o":
            coor.append(xy)
            windows.blit(top2, (x, y))
        elif ligne == "m":
            coor_mur.append(xy)
            windows.blit(mur, (x, y))
        elif ligne == "c":
            coor.append(xy)
            coor_mur.append(xy)
            windows.blit(danger, (x, y))



    """"test de positionnement de MacGyver par rapport aux éléments l'entourant"""

    if position_precise == objet_aleatoire:
        objet_aleatoire = (750, 750)
        counter += 1
        text = font.render("objets ramasses : " + str(counter), True, (255, 255, 255))
        rect_text = text.get_rect()

    elif position_precise == objet_aleatoire2:
        objet_aleatoire2 = (750, 750)
        counter += 1
        text = font.render("objets ramasses : " + str(counter), True, (255, 255, 255))
        rect_text = text.get_rect()

    elif position_precise == RANDOM_OBJECT3:
        RANDOM_OBJECT3 = (750, 750)
        counter += 1
        text = font.render("objets ramasses : " + str(counter), True, (255, 255, 255))
        rect_text = text.get_rect()

    if position_precise in coor_mur:
        if vie > 0:
            vie -= 4
            text2 = font.render("SANTE : " + str(vie), True, (255, 255, 255))

    if vie <=0:
        position_over = (0, 0)
        continuer = 0


    if position_precise == Gardien_conversion and counter < 3:
        position_over = (0, 0)
        continuer = 0

    if position_precise == Gardien_conversion and counter == 3:
        position_win = (0, 0)

    """"Refresh"""


    windows.blit(text, (20, 715))
    windows.blit(text2, (550, 715))
    windows.blit(MacGyver, (position_perso))
    windows.blit(aiguille, (objet_aleatoire2))
    windows.blit(boussole, (RANDOM_OBJECT3))
    windows.blit(ether, (objet_aleatoire))
    windows.blit(over, (position_over))
    windows.blit(win, (position_win))
    pygame.display.flip()