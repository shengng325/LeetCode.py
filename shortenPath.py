def shortenPath(path):
	isAbsPath = path[0] == "/"
	tokens = filter(isImportant, path.split('/'))
	stack = []
	if isAbsPath:
		stack.append("")
	for token in tokens:
		if token == "..":
			if not len(stack) or stack[-1] == "..":
				stack.append(token)
			elif stack[-1] != "":
				stack.pop()
		else:
			stack.append(token)
	if len(stack) == 1 and stack[0] == "":
		return "/"
	return "/".join(stack)

def isImportant(token):
	return len(token) > 0 and token != '.'

path = "/../../foo/../../bar/ba"
results = shortenPath(path) # /bar/ba
print(results)	
	
