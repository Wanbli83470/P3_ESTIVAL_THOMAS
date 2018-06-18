#! /usr/bin/env python3
#!/usr/bin/env python
from random import choice
chemin = "n.txt"
position = [350,350]

ouverture = open(chemin, 'r')
SQUARE_X = 0
SQUARE_Y = 0

case = [SQUARE_X, SQUARE_Y]

x = SQUARE_X * 50
y = SQUARE_Y * 50

xy = [x,y]

LOCATION_STARTING = []
position_arrivee = []
coor = []
LOCATION_WALL = []

for ligne in ouverture.read():
	x = SQUARE_X * 50
	y = SQUARE_Y * 50

	SQUARE_X = SQUARE_X +1

	if SQUARE_X > 15 :
		SQUARE_X = 0
		SQUARE_Y = SQUARE_Y + 1

	case = [SQUARE_X, SQUARE_Y]
	xy = [x,y]

	if ligne == "d":
		LOCATION_STARTING.append(xy)
	elif ligne == "a":
		position_arrivee.append(xy)
	elif ligne == "o":
		coor.append(xy)
	elif ligne == "m":
		LOCATION_WALL.append(xy)

RANDOM_OBJECT = (choice(coor))
RANDOM_OBJECT2 = (choice(coor))
RANDOM_OBJECT3 = (choice(coor))
objet_aleatoire4 = (choice(coor))
"""RANDOM_OBJECT3"""
MG_conversion = LOCATION_STARTING[0]
MG_x = MG_conversion[0]
MG_y = MG_conversion[1]
Gardien_conversion = position_arrivee[0]
