from heapq import *
import heapq
class Solution:
    def slidingWindowMedian(self, array, k):
        greaterHeap = []
        smallerHeap = []
        medians = []
        for i in range(len(array)):
            curValue = array[i]
            if not len(smallerHeap):
                smallerHeap.append(-curValue)
            elif curValue < -smallerHeap[0]:
                heapq.heappush(smallerHeap, -curValue) # maxHeap, value has to be -ve
            else:
                heapq.heappush(greaterHeap, curValue)

            self.balanceHeap(smallerHeap, greaterHeap)
            if i >= k - 1:
                curMedian = self.getMedian(smallerHeap, greaterHeap)
                medians.append(curMedian)
                self.removeValue(smallerHeap, greaterHeap, array[i - k + 1])
                self.balanceHeap(smallerHeap, greaterHeap)
        return medians

    def balanceHeap(self, smallerHeap, greaterHeap):
        if len(smallerHeap) - len(greaterHeap) > 1:
            valueRemoved = heapq.heappop(smallerHeap)
            heapq.heappush(greaterHeap, -valueRemoved)
        elif len(greaterHeap) - len(smallerHeap) > 0:
            valueRemoved = heapq.heappop(greaterHeap)
            heapq.heappush(smallerHeap, -valueRemoved)

    def getMedian(self, smallerHeap, greaterHeap):
        if len(smallerHeap) > len(greaterHeap):
            median = -smallerHeap[0]
        else:
            median = (-smallerHeap[0] + greaterHeap[0]) / 2
        return median

    def removeValue(self, smallerHeap, greaterHeap, value):
        if value <= -smallerHeap[0]:
            smallerHeap.remove(-value)
            heapq.heapify(smallerHeap)
        else:
            greaterHeap.remove(value)
            heapq.heapify(greaterHeap)

array = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
results = s.slidingWindowMedian(array, k)
print(results)