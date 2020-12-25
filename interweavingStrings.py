def interweavingStrings(one, two, three):
	return interweavingStringsHelper(one, two, three, 0, 0, 0)

def interweavingStringsHelper(one, two, three, ptrOne, ptrTwo, ptrThree):
	while ptrThree < len(three):
		isEqualOne = ptrOne < len(one) and three[ptrThree] == one[ptrOne]
		isEqualTwo = ptrTwo < len(two) and three[ptrThree] == two[ptrTwo]   
		if isEqualOne and isEqualTwo:
			withPtrOne = interweavingStringsHelper(one, two, three, ptrOne+1, ptrTwo, ptrThree+1)
			withPtrTwo = interweavingStringsHelper(one, two, three, ptrOne, ptrTwo+1, ptrThree+1)
			return withPtrOne or withPtrTwo
		elif isEqualOne:
			ptrOne+=1
		elif isEqualTwo:
			ptrTwo+=1
		else:
			return False
		ptrThree+=1
	return ptrOne == len(one) - 1 and ptrTwo == len(two) - 1


one = "algoexpert"
three = "your-algodream-expertjo"
two = "your-dream-job"
results = interweavingStrings(one, two, three)
print(results)