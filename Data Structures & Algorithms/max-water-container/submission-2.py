class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_vol = 0
        while start<end:
            w = end-start
            h = min(heights[start], heights[end])
            vol = w*h
            max_vol=max(vol, max_vol)
            if heights[start]<=heights[end]:
                start+=1
            else:
                end-=1
        return max_vol
