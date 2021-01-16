#Sujet: Gram & Lang - Projet L3
#Auteurs: TAYLOR Matt / SOCHAJ Yoann
#Date: 14/01/2021

#AFN pour tester nos fonctions
afn0 = 	[ [0,"a",0], [0,"a",2], [0,"b",1], [1,"b",0], [1,"b",3], [2,"a",3], [2,"b",1], [3,"a",3], [3,"b",1] ]
listEtat0 = [0,1,2,3]
listTransition0 = ["a","b"]


afn1 = [ [0,"a",0],[0,"b",0],[0,"a",1],[1,"b",2] ]
listEtat1 = [0,1,2]
listTransition1 = ["a", "b"]

#import
from itertools import islice
from pathlib import Path

#fonction pour lire le fichier texte
def readFile(name):
	listEtat = []
	listTransitions = []
	listEtatTerminaux = []
	listAFN = []
	compteur = 0
	with open(name+".txt", "r") as f:
		for line in f:
			if(compteur == 0):
				firstLine = line.split()
				for i in range(len(firstLine)):
					listEtat.append(firstLine[i])
				compteur +=1
			elif(compteur == 1):
				secondLine = line.split()
				for i in range(len(secondLine)):
					listTransitions.append(secondLine[i])
				compteur +=1
			elif(compteur == 2):
				thirdLine = line.split()
				for i in range(len(thirdLine)):
					listEtatTerminaux.append(thirdLine[i])
				compteur +=1
			else:
				for x in line.split():
					if x.isdigit():
						res = convert(x)
						listAFN.append(res)
					else:
						listAFN.append(x)
	return listEtat, listTransitions, listAFN, listEtatTerminaux

#fonction qui permet de convertir du "text" en int si c'est un entier (enlever les guillemets)
def convert(text):
	try:
		return int(text)
	except ValueError:
		return text

#fonction qui renvoie une liste remplis de 3 de longueur listAFN renvoye de la fonction readFile, elle va nous servir pour separer la liste en sous-listes
def customArr(fileName):
	a, b, c, d = readFile(fileName)
	res = []
	for i in range(int(len(c)/3)):
		res.append(3)
	return res

#fonction pour trouver la destination d'une transition en specifiant le depart et le charactere
def findPath(afn, list, char, printV):
	res  = []
	for i in range(len(afn)):
		for state in list:	
			if(afn[i][0] == state and afn[i][1] == char):
				if(afn[i][2] not in res):
					res.append(afn[i][2])
	if(res != [] and printV):
		print("From", list, "with", char, "->", res)
	return res

#fonction principale qui regroupe le tout
def afn2afd(afn):
	listA=[[0]]
	listB=[[0]]
		
	for i in range(len(listEtat1)):
		resA=findPath(afn,listA[i],"a", 0)
		resB=findPath(afn,listB[i],"b", 0)

		if(resA not in listA and resA != []):
			listA.append(resA)
		if(resA not in listB and resA != []):
			listB.append(resA)
	
		if(resB not in listB and resB != []):
			listB.append(resB)
		if(resB not in listA and resB !=[]):
			listA.append(resB)

	print("Liste des etats:", listA)
	for i in range (len(listA)):
		findPath(afn, listA[i], "a", 1)

	for i in range (len(listB)):
		findPath(afn, listB[i], "b", 1)
	
# **** MAIN ****
def main():
	while(1):
		try:
			fileName = (input("Enter file name: (without .txt)\n"))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		if (not Path(fileName+".txt").is_file()): #on verifie que le fichier existe
			print("File does not exist.")
			continue
		else:
			break

	a, b, c, d = readFile(fileName)
	print("Etats:", a)
	print("Alphabet:", b)
	print("Etat(s) Terminaux:", d)

	splitL = customArr(fileName)
	newC = iter(c)
	res = [list(islice(newC, size)) for size in splitL ]

	print("AFN:", res, "\n")

	afn2afd(res)

main()