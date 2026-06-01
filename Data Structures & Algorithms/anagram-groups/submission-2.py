class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        sol = []
        count = 0
        for i,v in enumerate(strs):
            if "".join(sorted(v)) in map:
                map["".join(sorted(v))].append(i)
            else:
                map["".join(sorted(v))] = [i]
        for key, value in map.items():
            sol.append([])
            for x in value: 
                sol[count].append(strs[x]) 
            count += 1
        print(sol)
        return sol



