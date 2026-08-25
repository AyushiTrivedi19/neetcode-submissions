class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for i in strs:
            s = "".join(sorted(i))
            if s not in result:
                result[s] = []
            result[s].append(i)
        return list(result.values())