def knapstackFruit(items, capacity):
	table = [ [0]*(capacity + 1) for _ in range(len(items) + 1) ]
	for i in range( len(items) ):
		for j in range( capacity + 1 ):
			curProfit = items[i][0] 
			curWeight = items[i][1]
			if j < curWeight:
				table[i + 1][j] = table[i][j]
			else:
				table[i + 1][j] = max(table[i][j], table[i][j - curWeight] + curProfit)
	k = len(table) - 1
	curCapacity = capacity
	selected = []
	while k > 0:
		if table[k][curCapacity] != table[k-1][curCapacity]:
			selected.insert(0, k - 1)
			curCapacity-=items[k - 1][1]
		k-=1
	return [table[-1][-1], selected]

	


items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10
results = knapstackFruit(items, capacity)
print(results)