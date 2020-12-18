def allSubsetSum(array):
    subsetSumArray = []
    allSubsetSumHelper(array, 0, subsetSumArray, 0)
    return subsetSumArray

def allSubsetSumHelper(array, idx, subsetSumArray, curSum):
    if idx >= len(array):
        subsetSumArray.append(curSum)
        return 
    allSubsetSumHelper(array, idx + 1, subsetSumArray, array[idx] + curSum)
    allSubsetSumHelper(array, idx + 1, subsetSumArray, curSum)

array = [2, 4, 5]
results = allSubsetSum(array)
print(results)