class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        arr =[[]]
        for i,v in enumerate(strs):
            if "".join(sorted(v)) in map: 
                map["".join(sorted(v))].append(i)
            else: 
                map["".join(sorted(v))] = [i]
        result = []
        for indices in map.values():
            group = [strs[idx] for idx in indices]
            result.append(group)  
        return result

