# Last updated: 8/31/2026, 1:58:23 PM
class Solution:
    def maxDistance(self, arr: List[List[int]]) -> int:
        min_val=arr[0][0]
        max_val=arr[0][-1]
        ans=0
        for i in range(1,len(arr)):
            cur_min =arr[i][0]
            cur_max =arr[i][-1]
            ans=max(ans,cur_max-min_val,max_val-cur_min)
            min_val=min(cur_min,min_val)
            max_val=max(cur_max,max_val)
        return ans