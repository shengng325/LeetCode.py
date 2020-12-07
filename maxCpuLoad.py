def maxCpuLoad(arrays):
    maxCpu = 0
    arrays.sort(key=lambda x: x[0])
    start = 0
    end = 1
    load = 2
    maxCpu = arrays[0][load]
    i = 0
    while i < len(arrays):
        loadCount = arrays[i][load]
        while i + 1 < len(arrays) and arrays[i][end] > arrays[i + 1][start]:
            i+=1
            loadCount+=arrays[i][load]
        maxCpu = max(maxCpu, loadCount)
        i+=1
    return maxCpu

arrays = [[1,2,2], [3,4,1], [5,6,5]]
results = maxCpuLoad(arrays)
print(results)