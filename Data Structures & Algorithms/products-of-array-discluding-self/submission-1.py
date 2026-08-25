class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]

        right = 1
        for j in range(len(nums)-1,-1,-1):
            left[j]*=right
            right*=nums[j]

        return left 