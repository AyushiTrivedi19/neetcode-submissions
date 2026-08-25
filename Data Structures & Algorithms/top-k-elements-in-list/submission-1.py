class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] +=1
        s = sorted(result.items(), key = lambda pair: pair[1], reverse = True)
        li = list(pair[0] for pair in s[:k])
        return li