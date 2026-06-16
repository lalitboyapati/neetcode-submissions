class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for x in strs:
            sortedx = "".join(sorted(x))
            sol[sortedx].append(x)
        return list(sol.values())