# O(N) T
# O(N) S
def stringAnagrams(string, pattern):
    patternChars = {}
    for char in pattern:
        if char not in patternChars:
            patternChars[char] = 0
        patternChars[char]+=1
    
    left = matched = 0
    anagramsIdx = []
    for right in range( len(string) ):
        if right - left + 1 > len(pattern):
            if string[left] in patternChars:
                if patternChars[string[left]] == 0:
                    matched -=1
                patternChars[string[left]]+=1
            left+=1
        if string[right] in patternChars:
            patternChars[string[right]]-=1
            if patternChars[string[right]] == 0:
                matched+=1
        if matched == len(patternChars):
            anagramsIdx.append(left)
    return anagramsIdx     

string = "abbcabc"
pattern = "abc"
results = stringAnagrams(string, pattern)
print(results)