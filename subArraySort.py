def subarraySort(array):
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	for i in range( len(array) ):
		if not inOrder(array, i):
			minOutOfOrder = min(minOutOfOrder, array[i])
			maxOutOfOrder = max(maxOutOfOrder, array[i])
	if minOutOfOrder == float("inf"):
		return [-1, -1]
	i = 0
	j = len(array) - 1
	while minOutOfOrder >= array[i]:
		i+=1
	while maxOutOfOrder <= array[j]:
		j-=1
	return [i, j]
		
def inOrder(array, idx):
	if idx == 0:
		if len(array) > 1:
			return array[0] <= array[1]
		return True
	elif idx == len(array) - 1:
		return array[-2] <= array[-1]
	return array[idx - 1] <= array[idx] and array[idx] <= array[idx + 1]

var = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
results = subarraySort(var)
print(results)
lambda x: expression