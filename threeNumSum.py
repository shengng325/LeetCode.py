# O(N^2) T
# O(N) S
def threeNumSum(array, target):
    sums = []
    array.sort()
    for i in range( len(array) - 2 ):
        twoNumTarget = target - array[i]
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[left] + array[right] == twoNumTarget:
                sums.append([array[i], array[left], array[right]])
                break
            elif array[left] + array[right] < twoNumTarget:
                left+=1
            else:
                right-=1
    return sums

array = [-3, 0, 1, 2, 2, 2, -1, 1, -2]
target = 0
results = threeNumSum(array, target)
print(results)