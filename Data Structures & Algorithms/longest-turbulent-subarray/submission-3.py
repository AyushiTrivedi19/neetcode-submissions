class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        max_count=1
        if len(arr)<2:
            return max_count
        prev_sign = arr[1]-arr[0]
        for R in range(1,len(arr)):
            curr_sign = arr[R]-arr[R-1]
            sign = curr_sign*prev_sign
            if curr_sign==0:
                L=R
            elif sign >0:
                L=R-1
            prev_sign = curr_sign
            max_count = max(max_count, R-L+1)
        return max_count