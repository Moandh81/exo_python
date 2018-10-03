#!/usr/bin/python
# -*- coding:Utf-8 -*-

# écrire un programme qui va scinder une liste
# contenant des chaines de caracteres
# en deux listes
# la premiere contiendra les chaines de moins de 6 caracteres
# la deuxième contiendra les chaines de plus de 6 chaines de caracteres

liste=["jean", "maximilien", "brigitte", "sonia", "jean-pierre", "sandra"]

liste_over_6=[]
liste_under_6=[]

i=0

while i<len(liste):
	if(len(liste[i]) >= 6):
		liste_over_6.append(liste[i])
	else:
		liste_under_6.append(liste[i])
	
	i=i+1

print(liste_over_6)
print(liste_under_6)
	