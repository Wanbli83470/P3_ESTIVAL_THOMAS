from constantes import *
import pygame
from pygame.locals import *


class level:
	def __init__(self, fichier):

	def generate(self):
		with open(self.fichier, "r") as fichier:
			structure_niveau = []

			for ligne in fichier:
				ligne_niveau = []
				for sprite in ligne:
					if sprite != '\n':
						ligne_niveau.append(sprite)
				structure_niveau.append(ligne_niveau)
			self.structure = structure_niveau

	def screen(self):



class perso:
	def __init__(self)











    fichier = "n.txt"

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
        x = case_x * size_sprite
        y = case_y * size_sprite

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