class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #key: numbers in nums ; value: index in nums each number belongs to 
        for i,v in enumerate(nums):
            diff = target - v
            if diff in map:
                return [map[diff], i]
            map[v] = i
        return ""


        
            

        