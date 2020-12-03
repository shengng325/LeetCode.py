# O(N) T
# O(N) S
def permutationInString(string, pattern):
    patternChars = {}
    for char in pattern:
        if char not in patternChars:
            patternChars[char] = 0
        patternChars[char]+=1
    left = 0
    matched = 0
    for right in range( len(string) ):
        if right >= len(pattern):
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
            return True
    return False

"abcdxabcde"
"abcdeabcdx"

string = "abcdxabcde"
pattern = "abcdeabcdx"
results = permutationInString(string, pattern)
print(results)