#!/usr/bin/python
# -*- coding:Utf-8 -*-

somme=0
print("insérer le premier entier :", end="")
first=input()


print("insérer le deuxième entier :", end="")
last=input()

liste=[int(first),int(last)]

for i in range(min(liste), max(liste)+1):
	if ( (i % 5) == 0 ) or ( (i % 3) == 0 ):
		somme = somme + i

print(str(somme))



