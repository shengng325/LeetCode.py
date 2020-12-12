def letterCasePermutations(string):
    permutations = [string]
    for i in range( len(string) ):
        if not string[i].isalpha():
            continue
        for j in range( len(permutations) ):
            perm = permutations[j][:i] + string[i].swapcase() + permutations[j][i+1:]
            permutations.append(perm)
    return permutations

string = "ab7c"
results = letterCasePermutations(string)
print(results)