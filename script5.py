# -*- coding:Utf-8 -*-


# écrivez un programme qui détermine si une chaine contient la lettre s

chaine=" Hello World "
i=0

while i<len(chaine):
	if chaine[i]=="s":
		print("la chaine de caracteres contient bien la lettre s")

	else:
		print("la chaine de caracteres ne contient pas la lettre s") 
	i=i+1

	break	