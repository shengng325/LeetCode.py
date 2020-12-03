# O(N) T
# O(N) S
def subArrayAverage2(array, k):
	averages = []
	windowSum = 0
	for i in range(k):
		windowSum += array[i]
	averages.append(windowSum / k)

	for i in range(1, len(array) - k + 1):
		windowSum = windowSum - array[i - 1] + array[i - 1 + k]
		averages.append(windowSum / k)
	return averages

def subArrayAverage(array, k):
	averages = []
	windowSum = 0
	left = 0
	for right in range(len(array)):
		windowSum+=array[right]
		if right >= k - 1:
			averages.append(windowSum / k)
			windowSum-=array[left]
			left+=1
	return averages

array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
results = subArrayAverage(array, k)
print(results)