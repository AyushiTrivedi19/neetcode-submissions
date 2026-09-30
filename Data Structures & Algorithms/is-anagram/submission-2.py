class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = dict()
        if len(s) != len(t):
            return False 
        for i in s:
            if i in result:
                result[i] +=1
            else:
                result[i] = 1
        for i in t:
            if i in result and result[i] != 0:
                result[i] -=1
            else:
                return False
        return True
