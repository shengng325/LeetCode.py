# O(N + k) T
# O(1) S

def smallestSubArrayWithGivenSum(array, sum):
    arraySize = 1
    while arraySize <= len(array):
        left = 0
        windowSum = 0
        for right in range(len(array)):
            windowSum += array[right]
            if right - left + 1 > arraySize :
                windowSum -= array[left]
                if windowSum >= sum:
                    return arraySize
                left+=1
        arraySize+=1
    return 0

array = [2, 1, 5, 2, 3, 2]
sum = 7
results = smallestSubArrayWithGivenSum(array, sum)
print(results)