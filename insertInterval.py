def insertInterval(arrays, arrayToInsert):
        newIntervals = []
        arrays.append(arrayToInsert)
        left = 0
        start = arrays[0][0]
        end = arrays[0][1]
        isInsert = False
        for right in range( len(arrays) ):
            end = max(end, arrays[right][1])
            if not isInsert and arrayToInsert[0] <= end:
                if arrayToInsert[1] >= start:
                    start = min(start, arrayToInsert[0])
                    end = max(end, arrayToInsert[1])
                else:
                    newIntervals.append(arrayToInsert)
                isInsert = True
            if right + 1 < len(arrays) and arrays[right + 1][0] <= end:
                max(end, arrays[right + 1][1])
            else:
                newIntervals.append([start, end])
                left = right + 1
                if left < len(arrays):
                    start = arrays[left][0]
        return newIntervals

arrays = [[1,5]]
arrayToInsert = [0,0]
results = insertInterval(arrays, arrayToInsert)
print(results)