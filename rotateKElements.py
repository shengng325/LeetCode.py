def rotateKElements(array, k):
    k = k%len(array)
    for i in range(k + 1):
        array.append(array[i])
        array.remove(i)
    return array

array = [1,2,3,4,5]
k = 2
results = rotateKElements(array, k)
print(results)