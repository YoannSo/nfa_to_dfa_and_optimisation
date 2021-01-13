afn = 	[ [0,"a",0], 
		[0,"a",2], 
		[0,"b",1], 
		[1,"b",0], 
		[1,"b",3], 
		[2,"a",3], 
		[2,"b",1], 
		[3,"a",3], 
		[3,"b",1] ]

# for i in range (len(afn)):

# 	currentState = afn[i][0]
# 	currentChar = afn[i][1]
# 	if( i == len(afn)-1):
# 		break
# 	nextState = afn[i+1][0]
# 	nextChar = afn[i+1][1]

	

# 	if(currentState == nextState and currentChar == nextChar):
# 		print("Super Etat:", afn[i][2], afn[i+1][2])


def createListEtat(n):
	res = []
	for i in range (n):
		res.append(i)
	return res

def findPath(afn, list, char):
	res  = []
	mychar = "a"
	for i in range(len(afn)):
		for state in list:	
			if(afn[i][0] == state and afn[i][1] == char):
				if(afn[i][2] not in res):
					res.append(afn[i][2])
	print("From", list, "with", char, "->", res)
	#print("from", list, "->", res)
	return res



#do state 0 with a, b 
#do state ... (that was created from previous request) with a, b
#etc....
#if the answer from the function was already treated no longer need to do it again

#findPath(afn, [0], "a")
# findPath(afn, [1], "a")
# findPath(afn, [2], "a")
# findPath(afn, [3], "a")
#findPath(afn, [0], "b")
# findPath(afn, [1], "b")
# findPath(afn, [2], "b")
# findPath(afn, [3], "a")
# findPath(afn, [3], "b")

# print("\nfirst super Etat")
# findPath(afn,[0,2], "a")
# findPath(afn,[0,2], "b")

# print("\nsecond super Etat")
# findPath(afn,[0,3], "a")
# findPath(afn,[0,3], "b")

# print("\nthird super Etat")
# findPath(afn, [0,2,3], "a")
# findPath(afn, [0,2,3], "b")

#MANUAL TEST
findPath(afn, [0], "a")
findPath(afn, [0], "b")

# findPath(afn, [0,2], "a")
# findPath(afn, [0,2], "b")

# findPath(afn, [1], "a")
# findPath(afn, [1], "b")