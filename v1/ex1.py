#Sujet: Gram & Lang - Projet L3
#Auteurs: TAYLOR Matt / SOCHAJ Yoann
#Date: 14/01/2021

#import
from itertools import islice
import itertools
from pathlib import Path

#global
while(1):
		try:
			fileName = (input("Enter file name: (without .txt)\n")) #on demande le nom du fichier a l'user
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		if (not Path(fileName+".txt").is_file()): #on verifie que le fichier existe
			print("File does not exist.")
			continue
		else:
			break

#fonction pour lire le fichier texte
def readFile(name):
	listEtat = []
	listTransitions = []
	listEtatTerminaux = []
	listAFN = []
	compteur = 0 #le compteur va servir pour savoir a quelle ligne on se trouve
	with open(name+".txt", "r") as f:
		for line in f:
			if(compteur == 0):
				firstLine = line.split() #la premiere ligne correspond a la liste des etats
				for i in range(len(firstLine)):
					listEtat.append(firstLine[i])
				compteur +=1
			elif(compteur == 1):
				secondLine = line.split() #la deuxieme ligne correspond a l'alphabet
				for i in range(len(secondLine)):
					listTransitions.append(secondLine[i])
				compteur +=1
			elif(compteur == 2):
				thirdLine = line.split() #la troisieme ligne correspond a la liste des etats terminaux
				for i in range(len(thirdLine)):
					listEtatTerminaux.append(thirdLine[i])
				compteur +=1
			else: #le reste concerne l'AFN
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

#fonction pour trouver la destination d'une transition en specifiant le depart et le caractere
def findPath(afn, list, char, printV):
	res  = []
	for i in range(len(afn)):
		for state in list:	
			if(afn[i][0] == state and afn[i][1] == char):
				if(afn[i][2] not in res):
					res.append(afn[i][2])
	if(res != [] and printV):
		print("From", list, "with", char, "->", res) #on affiche les informations pour etre lu facilement par l'user
	return res

#fonction qui renvoie la sublist d'une list si elle contient une valeur passe en parametre
def getSublist(l, state):
	for sublist in l:
		for i in range(len(sublist)):
			if state in sublist:
				return sublist

#fonction principale qui regroupe le tout
def afn2afd(afn):
	a, b, c, listEtatTerminaux = readFile(fileName) #on utilise notre fonction definie au dessus pour lire notre fichier et avoir nos variables

	listA=[[0]] #on commence en partant des etats 0 pour "a" et "b"
	listB=[[0]]
		
	for i in range(3):
		resA=findPath(afn,listA[i],"a", 0)
		resB=findPath(afn,listB[i],"b", 0)

		if(resA not in listA and resA != []): #on verifie que le retour de la fonction findPath() n'est pas nul (list vide []) et qu'il n'est pas deja dans listA si c'est le cas on l'append
			listA.append(resA)
		if(resA not in listB and resA != []): #on le rajoute egalement a listB on verifiant les memes conditions
			listB.append(resA)
	
		if(resB not in listB and resB != []): #de meme pour listB
			listB.append(resB)
		if(resB not in listA and resB !=[]):
			listA.append(resB)

	print("Etats de l'AFD:", listA) #listA sera egal a listB a ce stade il suffit donc d'en afficher qu'un seul, il contient tous les etats de l'AFD

	newListEtatTerminaux = [] #on cree une nouvelle liste en remplacant les strings d'entiers par des "vrais" entiers
	for state in listEtatTerminaux:
		newListEtatTerminaux.append(convert(state))

	listEtatTerminauxAFD = [ getSublist(listA,x) for x in newListEtatTerminaux ] #on regarde si un etat terminal est dans un des etats nouvellement cree de l'AFD
	listEtatTerminauxAFD.sort() 
	listEtatTerminauxAFD = list(listEtatTerminauxAFD for listEtatTerminauxAFD, _ in itertools.groupby(listEtatTerminauxAFD)) #remove duplicates from list

	print("Etat(s) terminaux de l'AFD", listEtatTerminauxAFD) #on affiche la list des etats terminaux
	for i in range (len(listA)):
		findPath(afn, listA[i], "a", 1) #ensuite on affiche toutes les transitions pour chaque etat de nos listes

	for i in range (len(listB)):
		findPath(afn, listB[i], "b", 1)
	
# **** MAIN ****
def main():
	a, b, c, d = readFile(fileName) #on appelle notre fonction readFile pour avoir nos variables
	print("Etats:", a) #correspond a tous les etats (ligne 1 du fichier)
	print("Alphabet:", b) #correspond l'alphabet (ligne 2 du fichier)
	print("Etat(s) Terminaux:", d) #correspond a tous les etats terminaux (ligne 3 du fichier)

	splitL = customArr(fileName)
	newC = iter(c)
	res = [list(islice(newC, size)) for size in splitL ] #ces lignes permettent de remettre c en une liste de sous-listes

	print("AFN:", res, "\n") #on affiche l'AFN lu du fichier en forme de liste
	print("******* RESULTAT *******\n")
	afn2afd(res) #on appelle notre fonction principale sur notre AFN

main() #on lance le main!