class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for x in nums:
            map[x] += 1
        for i,v in map.items():
            freq[v].append(i)
        sol = []
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                sol.append(x)
                if len(sol) == k:
                    return sol




        


        


        

        





