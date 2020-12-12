def subsetsWithDuplicates(array):
    array.sort()
    subsets = [[]]
    for i in range( len(array) ):
        curStartIdx = len(subsets)
        if i - 1 >= 0 and array[i - 1] == array[i]:
            for k in range(prevStartIdx, prevEndIdx + 1):
                subsets.append(subsets[k] + [array[i]])
        else:
            for j in range( len(subsets) ):
                subsets.append(subsets[j] + [array[i]])
        prevStartIdx = curStartIdx
        prevEndIdx = len(subsets) - 1
    return subsets

array = [1, 5, 5]
results = subsetsWithDuplicates(array)
print(results)