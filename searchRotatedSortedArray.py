def searchRotatedSortedArray(array, key):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = ( left + right ) // 2
            if array[mid] == key:
                return mid
            elif array[left] <= array[mid]:
                if key >= array[left] and key <= array[mid]: 
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if key >= array[mid] and key <= array[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

array = [3,4,5,6,7,8,1,2]
key = 2
results = searchRotatedSortedArray(array, key)
print(results)