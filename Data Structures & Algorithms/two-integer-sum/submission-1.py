class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    total -=nums[i]