def smallestSubstringWithPattern(string, pattern):
    patternChars = {}
    for char in pattern:
        if char not in patternChars:
            patternChars[char] = 0
        patternChars[char]+=1

    left = 0
    matched = 0
    minLength = len(string) + 1
    for right in range( len(string) ):
        rightChar = string[right]
        if rightChar in patternChars:
            patternChars[rightChar]-=1
            if patternChars[rightChar] >= 0:
                matched+=1

        while matched == len(pattern):
            if right - left + 1 < minLength:
                minLength = right - left + 1
                subStrStart = left
            
            leftChar = string[left]
            if leftChar in patternChars:
                if patternChars[leftChar] == 0:
                    matched-=1
                patternChars[leftChar]+=1
            left+=1
    if minLength > len(string):
        return ""
    return string[subStrStart:subStrStart + minLength]

string = "abdcdabcdabc"
pattern = "abc"
results = smallestSubstringWithPattern(string, pattern)
print(results)