class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for x in nums:
            map[x] += 1
        for i, v in map.items():
            freq[v].append(i)
        rlist = []
        for i in range(len(nums), 0, -1):
            for x in freq[i]:
                rlist.append(x)
                if len(rlist) == k:
                    return rlist







        


        


        

        





