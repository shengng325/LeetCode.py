# O(NlogN) T
# O(N) S
def mergeIntervals(arrays):
    mergedIntervals = []
    arrays.sort(key=lambda array: array[0])
    left = right = 0
    maxEnd = arrays[0][1]
    for right in range( len(arrays) ):
        maxEnd = max(maxEnd, arrays[right][1])
        if right + 1 < len(arrays) and arrays[right + 1][0] <= maxEnd:
            maxEnd = max(maxEnd, arrays[right + 1][1])
        else:
            mergedIntervals.append([arrays[left][0], maxEnd])
            left = right + 1
    return mergedIntervals


arrays = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
results = mergeIntervals(arrays)
print(results)