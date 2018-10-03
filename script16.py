#!/usr/bin/python
# -*- coding:Utf-8 -*-

# un programme qui permet de prendre les valeurs d'un input utilisateur
# et de les utiliser pour remplir un tableau
# la saisie des valeurs se termine si l'utilisateur appuie sur la touche entrée

liste=[]



while True:
	valeur = input("Insérer la valeur souhaitée :")
	liste.append(valeur)
	if valeur ==  "":
		liste.pop()
		break

print(liste)