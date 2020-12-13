import heapq
def sortCharByFrequency(string):
        charFrequency = {}
        for i in range( len(string) ):
            if string[i] not in charFrequency:
                charFrequency[string[i]] = 0
            charFrequency[string[i]]+=1
        maxHeap = []
        for char, freq in charFrequency.items():
            heapq.heappush(maxHeap, (-freq, char))
        newStrList = []
        while len(maxHeap) > 0:
            charRemoved = heapq.heappop(maxHeap)
            for _ in range(-charRemoved[0]):
                newStrList.append(charRemoved[1])
        sortedStr = "".join(newStrList)
        return sortedStr

string = "Programming"
results = sortCharByFrequency(string)
print(results)