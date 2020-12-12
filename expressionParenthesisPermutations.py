def expressionParenthesisPermutations(string):
	result = []
	if '+' not in string and '-' not in string and '*' not in string:
		result.append(int(string))
	else:
		for i in range(0, len(string)):
			char = string[i]
			if not char.isdigit():
				leftParts = expressionParenthesisPermutations(string[0:i])
				rightParts = expressionParenthesisPermutations(string[i+1:])
				for part1 in leftParts:
					for part2 in rightParts:
						if char == '+':
							result.append(part1 + part2)
						elif char == '-':
							result.append(part1 - part2)
						elif char == '*':
							result.append(part1 * part2)
	return result


string = "2*3-4-5"
results = expressionParenthesisPermutations(string)
print(results)