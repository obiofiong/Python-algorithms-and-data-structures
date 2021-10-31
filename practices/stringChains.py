def findSubset(arr, i):
    longestSubset = ''
    for j in arr:
            if j == i:
                continue
            lenMatch = 0
            for k in j:
                if k in i:
                    lenMatch+=1
            if lenMatch == len(j):
                if len(j) > len(longestSubset):
                    longestSubset = j
            else:
                continue
    return longestSubset
def longestChain(arr):
    maxWord = ''
    for i in arr :
        if len(i) == 1:
            continue
        longestSubset = findSubset(arr, i)
        while len(longestSubset): 
            if len(longestSubset) > len(maxWord):
                maxWord = longestSubset
            longestSubset = findSubset(arr,longestSubset)
    return len(maxWord) + 1

test1 = ['a','and','an', 'bear']
test2 = ['a','b','ba','bca','bda', 'bdca']
test3 = ['a', '']

print(longestChain(test3))