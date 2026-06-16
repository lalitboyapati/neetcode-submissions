class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c)-ord("a")] += 1
            sol[tuple(count)].append(x)
        return list(sol.values())