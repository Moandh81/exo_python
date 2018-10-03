# -*- coding:Utf-8 -*-

# exercice sur les listes


t1= [31,30,31,30,31,30,31,30,31,30,31,30]
t2=['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']
t3=[]

i=0

while i<len(t2):
	t3.append(t2[i])
	t3.append(t1[i])
	i= i +1

print(t3)