#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import random
from constantes import *
from aleatoire import*

ether_x = random.randint(0,15)
ether_x = ether_x * 50
ether_y = random.randint(0,15)
ether_y = ether_y * 50
seringue_x = random.randint(0,15)
seringue_x = seringue_x * 50
seringue_y = random.randint(0,15)
seringue_y = seringue_y * 50

ether2 = (254,425)

liste_auto = [[0,50],
            [0,150],
            [0,400],
            [0,400],
            [0,550],
            [0,550],
            [0,650],
            [0,700],
            [50,50],
            [50,150],
            [50,200],
            [50,350],
            [50,400],
            [50,450],
            [50,500],
            [50,600],
            [50,650],
            [100,50],
            [100,150],
            [100,300],
            [100,350],
            [100,400],
            [100,500],
            [100,550],
            [100,600],
            [100,650],
            [150,0],
            [150,50],
            [150,100],
            [150,150],
            [150,250],
            [150,300],
            [150,350],
            [150,450],
            [150,550],
            [150,650],
            [200,150],
            [200,250],
            [200,650],
            [250,0],
            [250,50],
            [250,150],
            [250,250],
            [250,350],
            [250,400],
            [250,500],
            [250,550],
            [250,600],
            [250,650],
            [300,0],
            [300,50],
            [300,150],
            [300,250],
            [300,400],
            [300,650],
            [350,0],
            [350,50],
            [350,150],
            [350,250],
            [350,350],
            [350,400],
            [350,450],
            [350,500],
            [350,550],
            [350,650],
            [400,0],
            [400,50],
            [400,150],
            [400,250],
            [400,350],
            [400,550],
            [400,600],
            [400,650],
            [400,700],
            [450,0],
            [450,50],
            [450,100],
            [450,150],
            [450,200],
            [450,250],
            [450,350],
            [450,400],
            [450,450],
            [450,500],
            [450,700],
            [500,0],
            [500,250],
            [500,300],
            [500,550],
            [500,600],
            [500,700],
            [550,0],
            [550,100],
            [550,150],
            [550,200],
            [550,250],
            [550,300],
            [550,400],
            [550,550],
            [600,0],
            [600,100],
            [600,150],
            [600,200],
            [600,250],
            [600,300],
            [600,400],
            [600,550],
            [600,600],
            [600,650],
            [650,0],
            [650,100],
            [650,150],
            [650,200],
            [650,250],
            [650,300],
            [650,350],
            [650,400],
            [650,550],
            [700,0],
            [700,400],
            [700,450],
            [700,500],
            [700,550],
            [700,600],
            [700,650],
            [700,0],
            [700,50],
            [700,100],
            [700,150],
            [700,200],
            [700,250],
            [700,300],
            [700,350],
            [700,400],
            [700,550]],



pygame.init()
#couleur
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

#compteur
counter = 0
# coordonnées case_dangers
C7=[100,300]
C14=[100,650]
L6=[550,250]
N12=[650,550]
#vie
vie = 4
position_seringue=(750,750)
appartion_seringue=(650,750)
#Opening PyGame windows
windows = pygame.display.set_mode((size_windows,size_windows))
#name windows
pygame.display.set_caption(titre_fenetre)
#loading background
fond = pygame.image.load(image_fond)
windows.blit(fond, (0,0))
#loading MacGyver
MacGyver = pygame.image.load(image_MacGyver).convert_alpha()
position_perso = MacGyver.get_rect()
windows.blit(MacGyver, position_perso)
position_perso.y = (50)
position_perso.x = (0)
#loading Gardien
Gardien = pygame.image.load(image_Gardien).convert_alpha()
windows.blit(Gardien, (712,555))
#loading ether
seringue = pygame.image.load(image_seringue).convert_alpha()
windows.blit(seringue, (position_seringue))
#loading seringue
ether = pygame.image.load(image_ether).convert_alpha()
windows.blit(ether, (objet_aleatoire))
#loading aiguille
aiguille = pygame.image.load(image_aiguille).convert_alpha()
windows.blit(aiguille, (objet_aleatoire2))
#loading boussole
boussole = pygame.image.load(image_boussole).convert_alpha()
windows.blit(boussole, (objet_aleatoire3))
#loading Game over
over = pygame.image.load(image_gameover).convert_alpha()
windows.blit(over, (0,0))
position_over = (750,750)
#loading WIN
win = pygame.image.load(image_win).convert_alpha()
windows.blit(win, (0,0))
position_win = (750,750)
# objets ramasses
font=pygame.font.Font(None,50)
text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
rect_text = text.get_rect()
#compteur point de vie
points_de_vies = pygame.font.Font(None,50)
text2=font.render("SANTE : " + str(vie),True,(255,255,255))
rect_text2 = text2.get_rect()
#texte defaite
defaite=font.render("defaite",True,(255,255,255))
rect_text = defaite.get_rect()
position_texte = (750,750)
windows.blit(text,(20,715))
windows.blit(defaite,(750,750))
#loading arrivée
top = pygame.image.load(image_ouverture).convert()
windows.blit(top,(0,0))
#loading wall
mur = pygame.image.load(wall).convert()
windows.blit(mur,(0,0))
#loading case danger
danger = pygame.image.load(image_casedanger).convert()
windows.blit(danger,(0,0))
#loading parcours
top2 = pygame.image.load(image_depart).convert()
windows.blit(top,(0,0))

pygame.display.flip()




continuer = 1

while continuer == 1:

 
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN :
            
            if event.key == K_LEFT:
                if position_x > 0:
                    if valeur_suivante_gauche in coor:
                        position_perso = position_perso.move(-50,0)
                else :
                    print("erreur de deplacement")
            elif event.key == K_RIGHT:
                if position_x < 700:
                    if valeur_suivante_droite in coor:
                        position_perso = position_perso.move(50,0)
                else :
                    print("erreur de deplacement")
            elif event.key == K_UP:
                if position_y > 0:
                    if valeur_suivante_haut in coor:
                        position_perso = position_perso.move(0,-50)
                else :
                    print("erreur de deplacement")
            elif event.key == K_DOWN:
                if position_y < 700:
                    if valeur_suivante_bas in coor:
                        position_perso = position_perso.move(0,50)
                else :
                    print("erreur de deplacement")
    



    #Re-collage
 

    
    windows.blit(text,(20,715))
    windows.blit(text2,(550,715))

    windows.blit(defaite,(position_texte))
    windows.blit(over, (position_over))
    windows.blit(win, (position_win))
        #refresh
 


    position_precise = (position_perso[0:2])
    position_x = position_precise[0]
    position_y = position_precise[1]

    x50=(position_precise[0]+50)
    x_moins50=(position_precise[0]-50)

    y50=(position_precise[1]+50)
    y_moins50=(position_precise[1]-50)

    valeur_suivante_droite = [x50,position_y]
    valeur_suivante_gauche = [x_moins50,position_y]
    valeur_suivante_haut = [position_x,y_moins50]
    valeur_suivante_bas = [position_x,y50]

    chemin = "n.txt"

    ouverture = open(chemin, 'r')
    case_x = 0
    case_y = 0

    case = [case_x, case_y]

    x = case_x * 50
    y = case_y * 50

    xy = [x,y]

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
        xy = [x,y]

        if ligne == "d":
            position_depart.append(case)
            windows.blit(top,(x,y))
        elif ligne == "a":
            position_arrivee.append(xy)
            windows.blit(top,(x,y))
            windows.blit(Gardien, (x,y))
            coor.append(xy)
        elif ligne == "o":
            coor.append(xy)
            windows.blit(top2,(x,y))
        elif ligne == "m":
            coor_mur.append(xy)
            windows.blit(mur,(x,y))
        elif ligne == "c":
            coor.append(xy)
            coor_mur.append(xy)
            windows.blit(danger,(x,y))

    if position_precise == objet_aleatoire :
        objet_aleatoire = (750,750)
        counter += 1
        text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
        rect_text = text.get_rect()

    elif position_precise == objet_aleatoire2:
        objet_aleatoire2 = (750,750)
        counter += 1
        text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
        rect_text = text.get_rect()

    elif position_precise == objet_aleatoire3:
        objet_aleatoire3 = (750,750)
        counter += 1
        text=font.render("objets ramasses : " + str(counter),True,(255,255,255))
        rect_text = text.get_rect()

    if position_precise in coor_mur :
        print("detection mur danger")
        if vie > 0 :
            vie -=4
            text2=font.render("SANTE : " + str(vie),True,(255,255,255))

    if vie <=0:
        print("perdu")
        position_over = (0,0)
        continuer = 0

    if position_precise == [700,550] and counter < 3 :
        position_over = (0,0)
        continuer = 0

    if position_precise == [700,550] and counter == 3:
        position_win = (0,0)
        print("test")

    print (position_arrivee)
    print (position_precise)
    windows.blit(text,(20,715))
    windows.blit(text2,(550,715))
    windows.blit(MacGyver, (position_perso))
    windows.blit(aiguille, (objet_aleatoire2))
    windows.blit(boussole, (objet_aleatoire3))
    windows.blit(ether, (objet_aleatoire))
    windows.blit(seringue, (position_seringue))
    windows.blit(over, (position_over))
    windows.blit(win, (position_win))
    pygame.display.flip()