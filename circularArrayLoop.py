class Solution:
    def circularArrayLoop(self, array):
        for i in range(len(array)):
            isForward = array[i] > 0
            slow = fast = i

            while True:
                slow = self.findNext(array, slow, isForward)
                fast = self.findNext(array, fast, isForward)
                if fast != -1:
                    fast = self.findNext(array, fast, isForward)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
        return False

    def findNext(self, array, idx, isForward):
        nextIdx = (idx + array[idx]) % len(array)
        isNextForward = array[nextIdx] > 0
        if isNextForward != isForward or nextIdx == idx:
            return -1
        return nextIdx

array = [2,-1,1,2,2]
s = Solution()
results = s.circularArrayLoop(array)
print(results)