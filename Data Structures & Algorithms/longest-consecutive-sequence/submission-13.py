class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 
        max = 1
        trmax = 1
        nums = sorted(list(set(nums)))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                max += 1
                if max >= trmax:
                    trmax = max 
            else: 
                max = 1
        return trmax
