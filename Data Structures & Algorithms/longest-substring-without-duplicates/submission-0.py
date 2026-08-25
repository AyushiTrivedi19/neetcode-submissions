class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, K = 0, 0
        st = set()
        for R in range(len(s)):
            while s[R] in st:
                st.remove(s[L])
                L+=1
            st.add(s[R])
            K = max(K,R-L+1)
        return K
