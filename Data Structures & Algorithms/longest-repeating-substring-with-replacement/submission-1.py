class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = dict()
        longest = 0
        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]]=1
            else:
                count[s[right]]+=1
            window_length = right-left+1
            max_freq = max(count.values())
            while (window_length-max_freq)>k:
                count[s[left]]-=1
                left+=1
                window_length = right-left+1
                max_freq = max(count.values())
            longest = max(longest,window_length)
        return longest