import heapq

def mergeSortedArraysHeap(arrays):
        k = len(arrays)
        minHeap = []
        mergedArray = []
        for i in range(k):
            heapq.heappush(minHeap, (arrays[i][0], i, 0))
        while minHeap:
            valueRemoved, arrayIdx, prevIdx = heapq.heappop(minHeap)
            mergedArray.append(valueRemoved)
            if prevIdx + 1 < len(arrays[arrayIdx]):
                heapq.heappush(minHeap, (arrays[arrayIdx][prevIdx + 1], arrayIdx, prevIdx + 1))
        return mergedArray

arrays = [[1,4,5],[1,3,4],[2,6]]
results = mergeSortedArraysHeap(arrays)
print(results)