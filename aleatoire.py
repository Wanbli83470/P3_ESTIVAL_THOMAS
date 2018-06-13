from random import choice
chemin = "n.txt"
position = [350,350]

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
		position_depart.append(xy)
	elif ligne == "a":
		position_arrivee.append(xy)
	elif ligne == "o":
		coor.append(xy)
	elif ligne == "m":
		coor_mur.append(xy)

objet_aleatoire = (choice(coor))
objet_aleatoire2 = (choice(coor))
RANDOM_OBJECT3 = (choice(coor))
objet_aleatoire4 = (choice(coor))
"""RANDOM_OBJECT3"""
MG_conversion = position_depart[0]
MG_x = MG_conversion[0]
MG_y = MG_conversion[1]
Gardien_conversion = position_arrivee[0]
