class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best_price = 0
        for i in range(len(prices)):
            profit = prices[i]-lowest
            best_price = max(best_price, profit)
            lowest = min(lowest, prices[i])
        return best_price