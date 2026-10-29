class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = (n*(n+1))//2
        sumi = 0
        for i in nums:
            sumi += i
        return totalSum-sumi