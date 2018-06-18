import pygame
from pygame.locals import * 
from constantes import *
from random import choice
windows = pygame.display.set_mode((size_windows, size_windows))

class gardien(object):

	def generate(self):
		self.creation=pygame.image.load(image_Gardien).convert_alpha()

	def affiche(self):
		windows.blit(self.creation,(0,0))
"""
		elif self.ligne == "a":
	        position_arrivee.append(xy)
	        windows.blit(CORRIDOR, (x, y))
	        windows.blit(GUARDIAN, (x, y))
	        coor.append(xy)"""

class MacGyver(object):
	def generate(self):
		self.creation=pygame.image.load(SCREEN_MacGyver).convert_alpha()
		self.LOCATION_HERO = self.creation.get_rect()
		self.LOCATION_HERO.x = (0)
		self.LOCATION_HERO.y = (50)
		self.y = self.LOCATION_HERO[0]
		self.x = self.LOCATION_HERO[1]
		self.case_x = self.x/50
		self.case_y = self.y/50
	def affiche(self):
		windows.blit(self.creation,(self.LOCATION_HERO))
		print(self.x)
		print(self.y)
	def move(self,direction):
		if direction == 'droite':
			if self.case_x < (nombre_sprite_cote + 1):
				self.LOCATION_HERO = self.LOCATION_HERO.move(+50, 0)
				print(self.LOCATION_HERO)
		if direction == 'gauche':
			if self.case_x < (nombre_sprite_cote + 1):
				self.LOCATION_HERO = self.LOCATION_HERO.move(-50, 0)
				print(self.LOCATION_HERO)
		if direction == 'haut':
			if self.case_y < (nombre_sprite_cote + 1):
				self.LOCATION_HERO = self.LOCATION_HERO.move(0,-50)
				print(self.LOCATION_HERO)
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote + 1):
				self.LOCATION_HERO = self.LOCATION_HERO.move(0, +50)
				print(self.LOCATION_HERO)
		
class Grille(object):
	def parcours(self):
		self.fichier = "n.txt"
		self.open = open(self.fichier, 'r')
		self.wall = []
		self.x = 0
		for line in self.open.read():
			if line == "m":
				self.x = self.x + 1
				self.wall.append(self.x)


	def Random(self) :
		self.RANDOM_OBJECT = []
		self.RANDOM_OBJECT.append((choice(self.wall)))
		print(self.RANDOM_OBJECT)



	"""def mur(self):
		pass"""
"""class ElementGrille(object):
	def Random(self,wall) :
		self.RANDOM_OBJECT = (choice(self.wall))
		print(self.RANDOM_OBJECT)
	def Screen(self) :
		pass"""



struct = Grille()
struct.parcours()
struct.Random()

struct2 = Grille()
struct2.parcours()
struct2.Random()









"""
class ElementGrille()
	def generate(self):
		self.ceation=pygame.image.load(image_Gardien).convert_alpha()

	def affiche():

        if self.ligne == "o":
            coor.append(xy)
            windows.blit(CORRIDOR2, (x, y))
        elif self.ligne == "m":
            LOCATION_WALL.append(xy)
            windows.blit(mur, (x, y))
        elif self.ligne == "c":
            coor.append(xy)
            LOCATION_WALL.append(xy)
            windows.blit(danger, (x, y))
"""