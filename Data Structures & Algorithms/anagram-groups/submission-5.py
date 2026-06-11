class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for x in strs:
            sortedx = "".join(sorted(x))
            if sortedx in res:
                res[sortedx].append(x)
            else:
                res[sortedx] = [x]
        return list(res.values())
        
 