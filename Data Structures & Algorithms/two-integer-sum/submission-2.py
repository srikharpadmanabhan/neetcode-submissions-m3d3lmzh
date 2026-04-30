class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        set_of_nums = dict()

        for idx, num in enumerate(nums):
            if target - num in set_of_nums:
                return [set_of_nums[target-num], idx]
            
            set_of_nums[num] = idx
        
        