def intervalsIntersection(array1, array2):
        intersections = []
        first = second = 0
        start = 0
        end = 1
        while first < len(array1) and second < len(array2):
            while array2[second][start] > array1[first][end] or array1[first][start] > array2[second][end]:
                while array2[second][start] > array1[first][end]:
                    first+=1
                    if first > len(array1) - 1:
                        return intersections
                while array1[first][start] > array2[second][end]:
                    second+=1
                    if second > len(array2) - 1:
                        return intersections

            if array1[first][start] >= array2[second][start] and array1[first][start] <= array2[second][end]:
                startPt = array1[first][start]
            else:
                startPt = array2[second][start]

            if array1[first][end] < array2[second][end]:
                endPt = array1[first][end]
                first+=1
            else:
                endPt = array2[second][end]
                second+=1
            intersections.append([startPt, endPt])
        return intersections

array1 = [[6,7],[8,13],[15,19]]
array2 = [[1,2],[4,5],[11,13],[15,16],[17,19]]

results = intervalsIntersection(array1, array2)
print(results)