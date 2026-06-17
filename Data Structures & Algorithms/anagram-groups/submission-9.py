class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for x in strs:
            freq = [0] * 26
            for c in x:
                freq[ord(c) - ord('a')] += 1
            map[tuple(freq)].append(x)
        return list(map.values())

            




        
        