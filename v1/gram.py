class Etat:
	def __init__(self, numero):
		self.numero = numero

	def printEtat(self):
		print("Numero: ", self.numero)

class Transition:
	def __init__(self, depart, nom, fin):
		self.depart = depart
		self.nom = nom
		self.fin = fin

	def printTransition(self):
		print("Depart: ", self.depart.numero, "Nom: ", self.nom, "Fin: ", self.fin.numero)



E1 = Etat(1)
E2 = Etat(2)

T1 = Transition(E1, "a", E2)

#T1.printTransition()


def lireFichier():
	listEtat = []
	listTransitions = []
	listAFN = []
	compteur = 0
	with open("myAfn.txt", 'r') as f:
		for line in f:
			#print(line)
			if(compteur == 0):
				flSplit = line.split()
				for i in range (len(flSplit)):
					E = Etat(flSplit[i])
					listEtat.append(E)
				compteur +=1 
			elif(compteur == 1):
				slSplit = line.split()
				for i in range (len(slSplit)):
					listTransitions.append(slSplit[i])
				compteur +=1
			else:
				transitionsSplit = line.split()
				
				listAFN.append(Transition(rechercheEtat(listEtat,transitionsSplit[0]), transitionsSplit[1], rechercheEtat(listEtat,transitionsSplit[2])))
	print("Conversion en structure de donnee:\n")
	#printListAFN(listAFN)
	return listEtat, listTransitions, listAFN


def AFN2AFD():
	listEtat, listTransitions, listAFN = lireFichier()
	print("Tous les etats:")
	#printListEtat(listEtat)
	print("Toutes les transitions:")
	#printListTransitions(listTransitions)
	print("AFN:")
	printListAFN(listAFN)

	listSuperEtatA = []
	listSuperEtatB = []

	for i in range (len(listAFN)): #pour tous les etats on regarde vers ou il peuvent aller et avec a
		#print(i)
		if(listAFN[i].depart == listEtat[0] and listAFN[i].nom == "a"): #si on est sur la bonne ligne alors on regarde vers ou ils vont
			listSuperEtatA.append(listAFN[i].fin)

		if(listAFN[i].depart == listEtat[0] and listAFN[i].nom == "b"): #si on est sur la bonne ligne alors on regarde vers ou ils vont
			listSuperEtatB.append(listAFN[i].fin)
	
	print("super etats avec a en partant de l'etat 0")
	printListEtat(listSuperEtatA)
	print("super etats avec b en partant de l'etat 0")
	printListEtat(listSuperEtatB)





#def findSuperEtat(depart, nom):
	
def printListEtat(listEtat):
	for i in range (len (listEtat) ) :
		listEtat[i].printEtat()

def printListTransitions(listTransitions):
	for i in range (len (listTransitions) ) :
		print(listTransitions[i])

	
def printListAFN(listAFN):
	for i in range (len (listAFN) ) :
		listAFN[i].printTransition()


def rechercheEtat(l, num):
	for i in range (len(l)):
		if(l[i].numero == num):
			return l[i]


			
# print(listEtat[0].printEtat())

AFN2AFD()			
# print("Lecture de afn.txt:")
# lireFichier()

