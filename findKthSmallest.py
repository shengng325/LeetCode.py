import heapq

def findKthSmallest(array, k):
    maxHeap = []
    for i in range(k):
        maxHeap.append(-array[i])
    heapq.heapify(maxHeap)
    for i in range(k, len(array) - 1):
        if array[i] < -maxHeap[0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -array[i])
    return -maxHeap[0]

array = [5, 12, 11, -1, 12]
k = 3
results = findKthSmallest(array, k)
print(results)