class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chOne = defaultdict(int)
        chTwo = defaultdict(int)
        for x in s:
            chOne[x] += 1
        for x in t:
            chTwo[x] += 1
        return chOne == chTwo