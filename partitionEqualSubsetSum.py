def partitionEqualSubsetSumBF(array):
    sumOfArray = sum(array)
    if sumOfArray%2 != 0:
        return False
    return partitionHelper(array, 0, sumOfArray//2)

def partitionHelper(array, idx, sumLeft):
    if sumLeft == 0:
        return True
    if idx >= len(array) or sumLeft < 0:
        return False
    return partitionHelper(array, idx + 1, sumLeft - array[idx]) or partitionHelper(array, idx + 1, sumLeft)

def partitionEqualSubsetSum(array):
        sumOfArray = sum(array)
        if sumOfArray%2 != 0:
            return False
        return dfHelper(array, sumOfArray//2)

def dfHelper(array, targetSum):
        dpTable = [[False]*(targetSum + 1) for _ in range( len(array) + 1)]
        dpTable[0][0] = True
        for i in range( len(array) ):
            for curSum in range(targetSum + 1):
                if curSum < array[i]:
                    dpTable[i + 1][curSum] = dpTable[i][curSum]
                else:
                    dpTable[i + 1][curSum] = dpTable[i][curSum] or dpTable[i][curSum - array[i]]
        return dpTable[-1][-1]

array = [5,1,11,5]
results = partitionEqualSubsetSum(array)
print(results)