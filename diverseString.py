import heapq

def diverseString(a, b, c):
    strArray = []
    heap = [ (-a, 'a'), (-b, 'b'), (-c, 'c') ]
    heapq.heapify(heap)
    while heap[-1][0] == 0:
        heap.pop()
    prevChar = None
    consecutiveCount= 0
    count = 0
    char = 1

    while heap:      
        if heap[0][char] == prevChar and consecutiveCount >= 2:
            if len(heap) <= 1:
                return ""
            removed = heap.pop(1)
            strArray.append(removed[char])
            prevChar = removed[char]
            if -removed[0] - 1 != 0:
                heap.append( (removed[count]+1 , removed[char]) )
                heapq.heapify(heap)
            consecutiveCount = 1
            continue

        if heap[0][char] == prevChar:
            consecutiveCount+=1
        else:   
            consecutiveCount = 1
        removed = heapq.heappop(heap)
        strArray.append(removed[char])
        prevChar = removed[char]
        if -removed[count] - 1 != 0:
            heapq.heappush(heap, (removed[count]+1 , removed[char]))           
    return "".join(strArray)


a = 6
b = 1
c = 1
results = diverseString(a, b, c)
print(results)