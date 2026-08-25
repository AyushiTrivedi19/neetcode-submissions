class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        sumi = 0
        K = len(nums)+1
        for R in range(len(nums)):
            sumi+=nums[R]
            while sumi>=target:
                K = min(K,(R-L)+1)
                sumi-=nums[L]
                L+=1
        if K!=len(nums)+1:
            return K
        else:
            return 0
            