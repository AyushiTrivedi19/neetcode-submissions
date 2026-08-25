class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        maxi = 0
        while L<R:
            width = R-L
            curr_height = min(heights[L], heights[R])
            area = curr_height*width
            maxi = max(maxi, area)
            if heights[L]<heights[R]:
                L+=1
            else:
                R-=1
        return maxi  