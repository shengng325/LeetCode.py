# O(N) T
# O(k + 1) S
def longestSubstrWithKDistinctChar(string, k):
    charFreq = {}
    left = right = 0
    maxLength = 0
    for i in range( len(string) ):
        if string[i] not in charFreq:
            charFreq[string[i]] = 0
        charFreq[string[i]]+=1   

        while len(charFreq) > k:
            charToPop = string[left]
            left+=1
            charFreq[charToPop]-=1
            if charFreq[charToPop] <= 0:
                del charFreq[charToPop]
        maxLength = max(maxLength, right - left + 1)
        right+=1
    return maxLength

string = "araaci"
k = 2
results = longestSubstrWithKDistinctChar(string, k)
print(results)