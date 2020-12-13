def findKthSmallestInSortedMatrix(matrix, k):
    start = matrix[0][0]
    end = matrix[-1][-1]
    while start < end:
        midNum = ( start + end ) // 2
        smallerCount, lessThanNum, moreThanNum = countSmallerThan(matrix, midNum)
        if smallerCount == k:
            return lessThanNum
        elif k < smallerCount:
            end = lessThanNum
        else:
            start = moreThanNum
    return start

def countSmallerThan(matrix, number):
    count = 0
    lessThanNum = matrix[0][0] - 1
    moreThanNum = matrix[-1][-1] + 1
    row = 0
    col = len(matrix) - 1
    while col >= 0 and row < len(matrix):
        curNum = matrix[row][col]
        if curNum <= number:
            count+= col + 1
            row+=1
            lessThanNum = max(lessThanNum, curNum)
        else:
            col-=1
            moreThanNum = min(moreThanNum, curNum)
    return count, lessThanNum, moreThanNum

matrix = [
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
]
k = 4

results = findKthSmallestInSortedMatrix(matrix, k)
print(results)