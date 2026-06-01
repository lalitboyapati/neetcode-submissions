class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for x in nums: 
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        freq_list = []
        for key, value in map.items():
            freq_list.append((value,key))
        freq_list.sort(reverse=True)
        sol = []
        for i in range(k):
            sol.append(freq_list[i][1])
        return sol




