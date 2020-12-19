def longestCommonPrefix(strs):
    shortest = strs[0]
    prefix = ""
    for i in range( len(shortest) ):
        count = 0
        for s in strs:
            if s[i] == shortest[i]:
                count+=1
                if count == len(strs):
                    prefix+=shortest[i]
    return prefix

strs = ["jarva", "jarvascript", "jarychou"]
results = longestCommonPrefix(strs)
print(results)