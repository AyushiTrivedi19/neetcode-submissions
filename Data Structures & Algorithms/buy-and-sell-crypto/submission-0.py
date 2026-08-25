class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best_profit = 0
        for price in prices:
            profit = price - lowest
            best_profit = max(best_profit, profit)
            lowest = min(lowest, price)
        return best_profit