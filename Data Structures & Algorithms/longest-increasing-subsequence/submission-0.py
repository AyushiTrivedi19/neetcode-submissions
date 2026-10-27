class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def lis(i):
            if i in memo:
                return memo[i]
            
            best = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1+lis(j))

            memo[i] = best
            return best
        
        return max(lis(i) for i in range(len(nums)))