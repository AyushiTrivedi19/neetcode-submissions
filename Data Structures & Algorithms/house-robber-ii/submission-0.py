class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def robLine(houses):
            memo = {}
            def dp(i):
                if i >= len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i] = max(houses[i] + dp(i+2), dp(i+1))
                return memo[i]
            return dp(0)
        return max(robLine(nums[:len(nums)-1]), robLine(nums[1:len(nums)]))