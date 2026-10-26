class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in memo:
                return memo[remaining]
            
            best = float('inf')
            for c in coins:
                best = min(best, 1+dp(remaining -c))
            
            memo[remaining] = best
            return best
        
        res =  dp(amount)
        if res != float('inf'):
            return res
        else:
            return -1