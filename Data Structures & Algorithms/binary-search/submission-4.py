class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        end = len(nums) - 1

        while low <= end:

            mid = low + (end-low) // 2

            num = nums[mid]
            if num == target:
                return mid
            
            if low == end:
                return -1

            if num < target:
                low = mid + 1
            else:
                end = mid - 1
        
        return -1

            
    
