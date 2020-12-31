def underscorifySubstring(string, substring):
	# Write your code here.
	foundIdx = []
	outputStr = ""
	i = 0
	while i < len(string):
		if string[i] == substring[0] and i + len(substring) <= len(string):
			count = 0
			for j in range( len(substring) ):
				if string[i + j] == substring[j]:
					count+=1
				if count == len(substring):
					foundIdx.append([i, i + len(substring) - 1])
		i+=1
	j = 0
	lastUnderscore = 0
	while j < len(foundIdx):
		left = foundIdx[j][0]
		while j + 1 < len(foundIdx) and foundIdx[j][1] + 1 >= foundIdx[j + 1][0]:
			j+=1
		right = foundIdx[j][1] + 1
		outputStr += string[lastUnderscore:left] + "_" + string[left:right] + "_"
		lastUnderscore = right
		j+=1
	outputStr+=string[lastUnderscore:]
	return outputStr

string = "abababababababababababababaababaaabbababaa"
substring = "a"
results = underscorifySubstring(string, substring)
print(results)