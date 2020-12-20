def numbersInPi(pi, numbers):
	numbersHash = {number:True for number in numbers}
	minSpaces = numbersInPiHelper(pi, numbersHash, 0, {}) 
	return minSpaces if minSpaces < len(pi) else -1

def numbersInPiHelper(pi, numbers, firstIdx, cache):
	if firstIdx >= len(pi):
		return -1
	if firstIdx in cache:
		return cache[firstIdx]
	minSpaces = len(pi)
	for i in range( firstIdx, len(pi) ):
		curNum = pi[firstIdx: i + 1]
		if curNum in numbers:
			minSpacesAfterThis = numbersInPiHelper(pi, numbers, i + 1, cache)
			minSpaces = min(minSpaces, minSpacesAfterThis + 1)
	cache[firstIdx] = minSpaces
	return minSpaces
	
pi = "31415" 
numbers = ["3", "141", "5", "31", "415"]
results = numbersInPi(pi, numbers)
print(results)

def numbersInPi(pi, numbers):
    minSpaces = numbersInPiHelper(pi, numbers, 0) 
	return minSpaces if minSpaces < len(pi) else -1

def numbersInPiHelper(pi, numbers, firstIdx):
	if firstIdx >= len(pi):
		return -1
	minSpaces = len(pi)
	for i in range( firstIdx, len(pi) ):
		curNum = pi[firstIdx: i + 1]
		if curNum in numbers:
			minSpacesAfter = numbersInPiHelper(pi, numbers, i + 1)
			minSpaces = min(minSpaces, minSpacesAfter + 1)
	return minSpaces