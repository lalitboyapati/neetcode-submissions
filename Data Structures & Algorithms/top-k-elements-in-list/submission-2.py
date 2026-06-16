class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for x in nums:
            map[x] += 1
        arr = []
        for i , v in map.items():
            arr.append([v,i])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res

        
        

        





