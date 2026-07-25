# Last updated: 7/25/2026, 11:43:46 AM
1class Solution:
2    def maxDistance(self, arr: List[List[int]]) -> int:
3        min_val=arr[0][0]
4        max_val=arr[0][-1]
5        ans=0
6        for i in range(1,len(arr)):
7            cur_min =arr[i][0]
8            cur_max =arr[i][-1]
9            ans=max(ans,cur_max-min_val,max_val-cur_min)
10            min_val=min(cur_min,min_val)
11            max_val=max(cur_max,max_val)
12        return ans