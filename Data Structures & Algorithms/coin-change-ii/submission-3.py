class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        memo = [[-1 for i in range(amount + 1)] for i in range(len(coins) + 1)] 

        def helper(idx, amount_left):
            if amount_left == 0:
                return 1
            
            if idx >= len(coins):
                return 0
            
            if memo[idx][amount_left] != -1:
                return memo[idx][amount_left]
            
            res = 0

            if amount_left >= coins[idx]:
                res += helper(idx, amount_left - coins[idx])
                res += helper(idx+1, amount_left)
            
            memo[idx][amount_left] = res

            return res
        
        res = helper(0, amount)

        return res