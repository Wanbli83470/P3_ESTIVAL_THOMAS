#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import random
ether_x = random.randint(0,15)
ether_x = ether_x * 50
ether_y = random.randint(0,15)
ether_y = ether_y * 50
seringue_x = random.randint(0,15)
seringue_x = seringue_x * 50
seringue_y = random.randint(0,15)
seringue_y = seringue_y * 50



position = {'a2':[0,50],
            'a4':[0,150],
            'a8':[0,400],
            'a9':[0,400],
            'a11':[0,550],
            'a12':[0,550],
            'a13':[0,650],
            'a15':[0,700],
            "b2":[50,50],
            "b4":[50,150],
            "b5":[50,200],
            "b8":[50,350],
            "b9":[50,400],
            "b10":[50,450],
            "b11":[50,500],
            "b13":[50,600],
            "b14":[50,650],
            "c2":[100,50],
            "c4":[100,150],
            "c7":[100,300],
            "c8":[100,350],
            "c9":[100,400],
            "c11":[100,500],
            "c12":[100,550],
            "c13":[100,600],
            "c14":[100,650],
            "d1" :[150,0],
            "d2":[150,50],
            "d3":[150,100],
            "d4":[150,150],
            "d6":[150,250],
            "d7":[150,300],
            "d8":[150,350],
            "d9":[150,450],
            "d11":[150,550],
            "d14":[150,650],
            "e4":[200,150],
            "e6":[200,250],
            "e14":[200,650],
            "f1" :[250,0],
            "f2":[250,50],
            "f4":[250,150],
            "f7":[250,350],
            "f8":[250,400],
            "f11":[250,500],
            "f12":[250,550],
            "f13":[250,600],
            "f14":[250,650],
            "g1" :[300,0],
            "g2":[300,50],
            "g4":[300,150],
            "g6":[300,250],
            "g9":[300,400],
            "g14":[300,650],
            "h1" :[350,0],
            "h2":[350,50],
            "h4":[350,150],
            "h6":[350,250],
            "h8":[350,350],
            "h9":[350,400],
            "h10":[350,450],
            "h11":[350,500],
            "h12":[350,550],
            "h14":[350,650],
            "i1" :[400,0],
            "i2":[400,50],
            "i4":[400,150],
            "i6":[400,250],
            "i8":[400,350],
            "i12":[400,550],
            "i13":[400,600],
            "i14":[400,650],
            "i15":[400,700],
            "j1" :[450,0],
            "j2":[450,50],
            "j3":[450,100],
            "j4":[450,150],
            "j5":[450,200],
            "j6":[450,250],
            "j8":[450,350],
            "j9":[450,400],
            "j10":[450,450],
            "j11":[450,500],
            "j15":[450,700],
            "k1" :[500,0],
            "k6":[500,250],
            "k7":[500,300],
            "k11":[500,550],
            "k12":[500,600],
            "k15":[500,700],
            "l1" :[550,0],
            "l3":[550,100],
            "l4":[550,150],
            "l5":[550,200],
            "l6":[550,250],
            "l7":[550,300],
            "l9":[550,400],
            "l12":[550,550],
            "m1" :[600,0],
            "m3":[600,100],
            "m4":[600,150],
            "m5":[600,200],
            "m6":[600,250],
            "m7":[600,300],
            "m9":[600,400],
            "m12":[600,550],
            "m13":[600,600],
            "m14":[600,650],
            "n1" :[650,0],
            "n3":[650,100],
            "n4":[650,150],
            "n5":[650,200],
            "n6":[650,250],
            "n7":[650,300],
            "n8":[650,350],
            "n9":[650,400],
            "n12":[650,550],
            "o1" :[700,0],
            "o9":[700,400],
            "o10":[700,450],
            "o11":[700,500],
            "o12":[700,550],
            "o13":[700,600],
            "o14":[700,650],
            "p1" :[700,0],
            "p2":[700,50],
            "p3":[700,100],
            "p4":[700,150],
            "p5":[700,200],
            "p6":[700,250],
            "p7":[700,300],
            "p8":[700,350],
            "p9":[700,400],
            "p12":[700,550],
            }

recup2 = position.get(random.choice(position.keys()))
recup3 = position.get(random.choice(position.keys()))
recup4 = position.get(random.choice(position.keys()))
print(recup2)
print(recup3)
print(recup4)

pygame.init()
#couleur
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

#compteur
counter = 0
#Opening PyGame windows
windows = pygame.display.set_mode((750, 750))
#name windows
pygame.display.set_caption("Aider MacGyver a s'echapper")
#loading background
fond = pygame.image.load("fond.jpg")
windows.blit(fond, (0,0))
#loading MacGyver
MacGyver = pygame.image.load("MacGyver50PX.png").convert_alpha()
position_perso = MacGyver.get_rect()
windows.blit(MacGyver, position_perso)
position_perso.y = (50)
#loading Gardien
Gardien = pygame.image.load("Gardien50PX.png").convert_alpha()
windows.blit(Gardien, (712,555))
#loading ether
ether = pygame.image.load("ether.png").convert_alpha()
windows.blit(ether, (recup2))
#loading seringue
seringue = pygame.image.load("seringue.png").convert_alpha()
windows.blit(seringue, (recup3))
#loading aiguille
aiguille = pygame.image.load("aiguille.png").convert_alpha()
windows.blit(aiguille, (recup4))


chaine="Objets rammasses : " + str(counter)
font=pygame.font.SysFont("broadway",35,bold=False,italic=False)
text=font.render(chaine,1,(255,255,255))
windows.blit(text,(20,715))

pygame.display.flip()


continuer = 1

while continuer:

    


    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                position_perso = position_perso.move(-50,0)
            elif event.key == K_RIGHT:
                position_perso = position_perso.move(50,0)
            elif event.key == K_UP:
                position_perso = position_perso.move(0,-50)
            elif event.key == K_DOWN:
                position_perso = position_perso.move(0,50)
            if event.key == K_SPACE:
                print("BRAVO")
                counter = counter - 1
                print(counter)




    #Re-collage
    windows.blit(fond, (0,0))   
    windows.blit(MacGyver, position_perso)
    windows.blit(Gardien, (712,555))
    windows.blit(ether, (recup2))
    windows.blit(seringue, (recup3))
    windows.blit(text,(20,715))
    windows.blit(aiguille, (recup4))
        #refresh
    pygame.display.flip()
    #print(position_perso)

    position_precise = (position_perso[0:2])
    print(position_precise)
    print(counter)
    if position_precise == recup2:
        recup2 = (750,750)
    	counter += 1
    	# del ether fais planter le jeu
    elif position_precise == recup3 :
    	print("detection")
        recup3 = (750,750)
        counter += 1
    	# del ether fais planter le jeu
    	print(counter)
    elif position_precise == recup4:
        recup4 = (750,750)
        counter += 1
    	# del ether fais planter le jeu
    	print(counter)
    elif position_precise == [700,550] and counter == 3:
        print("fin du jeu")
        continuer = 0

    if counter == 3 :
    	print("objets tous recuperes")

    else:
    	print("pas de détéction")
        print("tout les objets ne sont pas rammasses")   
    if counter == 3 :
    	pass
    	#del Gardien

