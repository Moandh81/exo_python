
Les différents types de variables
entier, réel, chaine de caractere
type liste, type dictionnaire

un nom de variable doit commencer par une lettre

les lettres ordinaires sont autorisées


la casse est significative


pas de noms réservés



typage des variables
typage dynamique 


affectations multiples
et affectations paralleles


// : division entière 

 2 // 7 = 0

** opérateur de puissance :
12**2 = 144



la notion d'affectation 

= est un signe d'affectation
et non un signe d'égalité
comme en mathématique 

il n'est pas possible d'écrire

b + 1 = m

la variable doit etre à gauche
la valeur de l'expression à droite



le flux d'éxécution 

séquence d'instructions
séquence ou exécution conditionnelle


Les opérateurs de comparaison 

x == y 
x != y
x > y
x < y
x >= y
x  <= y



instructions composées et blocs d'instructions 

un commentaire en python commence
toujours par un dièse 



Les instructions répétitives

réaffectation 


répétitions en boucle :

l'instruction while


l'argument 'end'


pseudo commentaire au début du script
pour l'encodage utf-8




exercices de la page 55 à faire 
exercices de la page 60 à faire
exercices de la page 64 
exercices de la page 67
exercices de la page 77
https://www.practicepython.org/
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
https://www.w3resource.com/python-exercises/


les triples qutoes permettent
d'ecrire du texte sur plusieurs 
lignes sans le passage par 


accès aux caractères individuels

d'une chaine de caractrere


Pour accéder à un caractère bien déterminé, on utilise le nom de la variable qui contient la chaîne et
on lui accole, entre deux crochets, l’index numérique qui correspond à la position du caractère dans la
chaîne.



opérations élémentaires sur les chaines

la concaténation avec le signe +

déterminer la longueur d'une 
chaine de caracteres à l'aide 
de la fonction len()


fonction int()
convertir une chaine de caractere en entier

fonction float convertir une chaine
de caractere en nombre à virgule

exemple
ch  = '8765'
int(ch)



chapitre 2 : controle 

l'opérateur modulo : reste de la division



Les listes 

append
del()


Les fonctions prédéfinies

print("bonjour", "à", "tous", sep="*")
sep définir le séparateur
, le séparateur par défaut étant 
l'espace



intéraction avec l'utilisateur 
la fonction input()


la fonction input renvoie toujours
une chaine de caracteres






Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres
multiples de 3 et de 5 compris entre ces bornes. Prendre par exemple a = 0, b = 32 ; le résultat
devrait être alors 0 + 15 + 30 = 45.
Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5
compris entre les bornes a et b. Avec les bornes 0 et 32, le résultat devrait donc être : 0 + 3 + 5
+ 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.


1ere version  :

#######################################################################

nbre1 = input("introduisez le nombre1 :")
nbre1 = int(nbre1)

print(type(nbre1))

nbre2 = input("introduisez le nombre2 :")
nbre2 = int(nbre2)
print(type(nbre2))

liste=list(range(nbre1, nbre2 +1, 1))
print(liste)

resultat=[]

for x in range(nbre1,nbre2+1):
	if ((x % 5) == 0) and ((x % 3) == 0):
		resultat.append(x)

print(resultat)

somme = 0
i = 0
while i < (len(resultat)):
	somme = somme + resultat[i]
	i = i +1

print(somme)

#######################################################################


