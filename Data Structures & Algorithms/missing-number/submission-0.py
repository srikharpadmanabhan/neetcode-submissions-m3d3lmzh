class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)

        return ((N) * (N+1)) // 2 - sum(nums)