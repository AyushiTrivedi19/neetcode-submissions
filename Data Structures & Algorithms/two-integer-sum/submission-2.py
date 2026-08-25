class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        for i in range(len(nums)):
            com = target - nums[i]
            if com in result:
                return [result[com], i]
            else:
                result[nums[i]] = i