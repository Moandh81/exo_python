# -*- coding:Utf-8 -*-

# écrire  un script qui compte le nombre d'occurrences
# de la  lettre e dans un chaine

chaine = "Hello Everybody eeeee"

i=0
nbre=0

while i<len(chaine):
 	if chaine[i]== "e":
 	 	nbre=nbre+1

 	i=i+1 	 

print("la chaine contient "  + str(nbre)) 	