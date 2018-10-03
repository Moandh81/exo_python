#!/usr/bin/python
# -*- coding:Utf-8 -*-




# écrire un programme qui scinde une liste de nombres
# en deux listes
# la première va contenir les chiffres pairs
# l'autre va contenir les chiffres impaires


liste=[32,5,12,8,3,75,2,15]

liste_pair=[]
liste_impair=[]
i=0

while i<len(liste):
	if (liste[i] % 2) == 0:
		liste_pair.append(liste[i])
	else:
		liste_impair.append(liste[i])

	i= i+1

print(liste_pair)
print(liste_impair)	
