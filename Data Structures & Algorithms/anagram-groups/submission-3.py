class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        sol = []
        for i, v in enumerate(strs):
            sortedv = "".join(sorted(v))
            if sortedv in map:
                map[sortedv].append(i)
            else:
                map[sortedv] = [i]
        for idx in map.values():
            group = [strs[x] for x in idx]
            sol.append(group)
        return sol


