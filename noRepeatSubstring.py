def noRepeatSubstring(string):
    charFreq = {}
    maxLength = 0
    left = right = 0
    while right < len(string):
        curChar = string[right]
        if curChar not in charFreq:
            charFreq[curChar] = 0
        charFreq[curChar]+=1
        while charFreq[curChar] > 1:
            charFreq[string[left]]-=1
            left+=1
        maxLength = max(maxLength, right - left + 1 )
        right+=1
    return maxLength

string = "abccde"
results = noRepeatSubstring(string)
print(results)