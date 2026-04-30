class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        this_set = set()

        for num in nums:
            if num in this_set:
                return True

            this_set.add(num)
        return False