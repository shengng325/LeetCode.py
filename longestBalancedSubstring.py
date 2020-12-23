def longestBalancedSubstring(string):
	maxLength = 0
	idxStack = []
	idxStack.append(-1)

	for i in range(len(string)):
		if string[i] == "(":
			idxStack.append(i)
		else:
			idxStack.pop()
			if len(idxStack) == 0:
				idxStack.append(i)
			else:
				balancedSubstringStartIdx = idxStack[len(idxStack) - 1]
				currentLength = i - balancedSubstringStartIdx
				maxLength = max(maxLength, currentLength)
	return maxLength

string = "))())(())((())(())(("
results = longestBalancedSubstring(string)
print(results)