#!/usr/bin/python
# -*- coding:Utf-8 -*-

# une fonction qui calcule le nombre d'occurrences
# d'une lette dans une chaine de caracteres

def occurrences(car, ch):
	nc=0
	i=0
	while i<len(ch):
		if ch[i] == car:
			nc=nc+1
			i=i+1
	return nc		

print