class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chOne = {}
        chTwo = {}
        for x in s: 
            if x in chOne:
                chOne[x] += 1
            else:
                chOne[x] = 1
        for x in t:
            if x in chTwo:
                chTwo[x] += 1
            else: 
                chTwo[x] = 1
        return chOne == chTwo