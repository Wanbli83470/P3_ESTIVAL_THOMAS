#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import * 
from constantes import *
from aleatoire import 
fichier = "n"


class level:
	def __init__(self, fichier):
		self.fichier = fichier

	def generate(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau

	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(wall).convert()
		danger = pygame.image.load(dangerous_sprite).convert()
		depart = pygame.image.load(dangerous_sprite).convert()
		arrivee = pygame.image.load(dangerous_sprite).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * size_sprite
				y = num_ligne * size_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				elif sprite == 'c':
					fenetre.blit(danger, (x,y))
				num_case += 1
			num_ligne += 1



class perso:
	def __init__(self, mac):
		self.mac = pygame.image.load(MacGyver50PX.png).convert_alpha()
		self.case_x = 0
		self.case_y = 0
		self.x = MG_x
		self.y = MG_y

	def move(self, direction):
		if direction == "droite":
			if self.case_x < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					self.case_x += 1

		if direction == "gauche":
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1

		if direction == "haut":
			if self.case_y > 0:
				if self.niveau.structure[self.case_y][self.case_x] != 'm':
					self.case_y -= 1

		if direction == "bas":
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y][self.case_x] != 'm':
					self.case_y += 1