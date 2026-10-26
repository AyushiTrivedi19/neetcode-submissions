class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def dp(left, right):
            nonlocal count
            while left>=0 and right<len(s) and s[left]==s[right]:
                count +=1
                left-=1
                right+=1
            return count
        
        for i in range(len(s)):
            dp(i, i)
            dp(i, i+1)
        
        return count