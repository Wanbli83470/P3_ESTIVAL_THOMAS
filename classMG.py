#-*- coding:utf-8 -*-
import pygame
from pygame.locals import * 
from constantes import *
from random import choice
windows = pygame.display.set_mode((SIZE_WINDOWS, SIZE_WINDOWS))



class MacGyver:
	def __init__(self,LOCATION_HERO=0):
		self.LOCATION_HERO = LOCATION_HERO
	def generate(self):
		self.creation=pygame.image.load(SCREEN_MACGYVER).convert_alpha()
		self.LOCATION_HERO = self.creation.get_rect()
		self.LOCATION_HERO.x = (0)
		self.LOCATION_HERO.y = (50)
		self.x = self.LOCATION_HERO[0]
		self.y = self.LOCATION_HERO[1]
		self.case_x = self.x/50
		self.case_y = self.y/50
	def affiche(self):
		windows.blit(self.creation,(self.LOCATION_HERO))
	def move(self,direction):
		if direction == 'droite':
			self.LOCATION_HERO = self.LOCATION_HERO.move(+50, 0)
			
		if direction == 'gauche':
			self.LOCATION_HERO = self.LOCATION_HERO.move(-50, 0)
			
		if direction == 'haut':
			self.LOCATION_HERO = self.LOCATION_HERO.move(0,-50)

		if direction == 'bas':
			self.LOCATION_HERO = self.LOCATION_HERO.move(0, +50)
		
class Grille:



	def parcours(self):
		mur = pygame.image.load(WALL).convert()
		windows.blit(mur, (0, 0))

		CORRIDOR = pygame.image.load(SCREEN_CORRIDOR).convert()
		windows.blit(CORRIDOR, (0, 0))

		danger = pygame.image.load(SCREEN_DANGEROUS).convert()
		windows.blit(danger, (0, 0))

		CORRIDOR2 = pygame.image.load(SCREEN_ARRIVAL).convert()
		windows.blit(CORRIDOR, (0, 0))

		GUARDIAN = pygame.image.load(SCREEN_GARDUIAN).convert_alpha()
		windows.blit(GUARDIAN, (0, 0))

		chemin = "n.txt"
		position = [350,350]

		ouverture = open(chemin, 'r')
		SQUARE_X = 0
		SQUARE_Y = 0

		x = SQUARE_X * 50
		y = SQUARE_Y * 50

		xy = [x,y]

		LOCATION_STARTING = []
		self.position_arrivee = int
		self.coor = []
		self.LOCATION_WALL = []

		for ligne in ouverture.read():
			x = SQUARE_X * 50
			y = SQUARE_Y * 50

			SQUARE_X = SQUARE_X +1

			if SQUARE_X > 15 :
				SQUARE_X = 0
				SQUARE_Y = SQUARE_Y + 1

			xy = [x,y]

			if ligne == "d":
				LOCATION_STARTING.append(xy)
				windows.blit(CORRIDOR, (x, y))
			elif ligne == "a":
				self.position_arrivee = (xy)
				windows.blit(CORRIDOR, (x, y))
				windows.blit(GUARDIAN, (x, y))
			elif ligne == "o":
				self.coor.append(xy)
				windows.blit(CORRIDOR2, (x, y))
			elif ligne == "m":
				self.LOCATION_WALL.append(xy)
				windows.blit(mur, (x, y))
			elif ligne == "c":
				self.coor.append(xy)
				self.LOCATION_WALL.append(xy)
				windows.blit(danger, (x, y))
				

	def Random(self) :
		"""object 1 """
		self.RANDOM_OBJECT = []
		self.RANDOM_OBJECT = (choice(self.coor))
		return self.RANDOM_OBJECT

class ElementGrille(Grille):
	def __init__ (self,MyObject = pygame.image.load(SCREEN_ETHER).convert_alpha(),position = [0,0]):
		self.MyObject = MyObject
		self.position = position
	def generate(self, choix):
		self.MyObject = choix
	def random(self, random):
		self.position = random
	def affiche(self):
		windows.blit(self.MyObject, (self.position))	