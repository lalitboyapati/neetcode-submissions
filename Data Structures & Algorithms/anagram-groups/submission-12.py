class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for x in strs:
            arr = [0] * 26
            for c in x:
                sortedx = ord(c) - ord('a')
                arr[sortedx] += 1
            map[tuple(arr)].append(x)
        return list(map.values())


            




        
        