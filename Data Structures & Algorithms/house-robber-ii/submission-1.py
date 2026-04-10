class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums[0], nums[1])
        

        def helper(numbers):
            if not numbers:
                return 0
            M = len(numbers)
            memo = [0] * M
            if M == 1:
                return numbers[0]
            elif M == 2:
                return max(numbers[0], numbers[1])

            memo[0] = numbers[0]
            memo[1] = max(numbers[0], numbers[1])
            for i in range(2,len(numbers)):
                memo[i] = max(memo[i-1], numbers[i] + memo[i-2])
            
            print(memo)
            return memo[-1]
    

        return max(helper(nums[1:]), helper(nums[:-1]))
            


