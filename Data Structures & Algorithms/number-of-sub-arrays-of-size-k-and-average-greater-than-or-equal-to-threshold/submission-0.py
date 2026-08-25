class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        i = 0
        sumi = 0
        for j in range(len(arr)):
            sumi+=arr[j]
            if j-i+1>k:
                sumi-=arr[i]
                i+=1
            avg = sumi//k
            if j-i+1==k:
                if avg>threshold or avg==threshold:
                    count+=1
        return count

