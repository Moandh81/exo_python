# -*- coding:Utf-8 -*-


# script qui recopie une chaine
# dans un nouvelle variable 
# tout en l'inversant
# exemple : zorglub devient blugroz
# le script va déterminer si une parole est
# un palindrome

chaine="zorglub"

i= len(chaine)

while i > 0:
 	inv = print(chaine[i-1], end='')
 	i = i - 1 

print("\n")
if(inv == chaine):
	print("la chaine " + chaine + " est un palindrome")
else:
	print ("la chaine " + chaine + " n'est pas un palindrome")