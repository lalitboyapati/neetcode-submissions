class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}
        for x in strs:
            sortedx = "".join(sorted(x))
            if sortedx in sol:
                sol[sortedx].append(x)
            else:
                sol[sortedx] = [x]
        return list(sol.values())