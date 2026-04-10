class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()

        memo = {}

        def helper(amount_needed):
            if amount_needed in memo:
                return memo[amount_needed]
                
            if amount_needed < 0:
                return -1
            
            if amount_needed == 0:
                return 0
            
            min_so_far = -1
            for coin in coins[::-1]:

                out = 1 + helper(amount_needed - coin)
                if out == 0:
                    continue

                if min_so_far == -1 or out < min_so_far:
                    min_so_far = out
            
            memo[amount_needed] = min_so_far
            return min_so_far
        
        return helper(amount)