afn0 = 	[ [0,"a",0], 
		[0,"a",2], 
		[0,"b",1], 
		[1,"b",0], 
		[1,"b",3], 
		[2,"a",3], 
		[2,"b",1], 
		[3,"a",3], 
		[3,"b",1] ]
listEtat0=[0,1,2,3]
listTransition=["a","b"]


afn1 = [ [0,"a",0],[0,"b",0],[0,"a",1],[1,"b",2] ]
listEtat1 = [0,1,2]


def createListEtat(n):
	res = []
	for i in range (n):
		res.append(i)
	return res

def findPath(afn, list, char, printV):
	res  = []
	mychar = "a"
	for i in range(len(afn)):
		for state in list:	
			if(afn[i][0] == state and afn[i][1] == char):
				if(afn[i][2] not in res):
					res.append(afn[i][2])
	if(res != [] and printV):
		print("From", list, "with", char, "->", res)
	return res


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
afn2afd(afn0)