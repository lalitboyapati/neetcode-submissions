class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        max_val = 1
        diff = [1] * (len(nums) - 1)
        for i in range(len(nums)-1): 
            diff[i] = nums[i+1]-nums[i]
        for x in diff:
            if x == 1:
                count += 1
                if count >= max_val:
                    max_val = count
            else: 
                count = 1
        return max_val