# -*- coding:Utf-8 -*-


#  écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7
# en signalant au passage à l'aide d'une astérique ceux qui sont multiple de 3
# Exemple  7 14 21  * 28 35 42* 49


nbre=7
i=1

while i<=20:
	if ((nbre*i) % 3) == 0:
		print(str(nbre*i) + " *" , end=' ')
	else:
		print(str(nbre*i) , end=' ') 
	i=i+1	