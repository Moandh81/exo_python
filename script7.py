# -*- coding:Utf-8 -*-


# script qui permet de recopier une chaine
# en insérant des astériques 
# exemple : g*a*s*t*o*n*


chaine= "gaston"
i=0

while i<len(chaine):
	print(chaine[i] + "*", end='')
	i = i + 1