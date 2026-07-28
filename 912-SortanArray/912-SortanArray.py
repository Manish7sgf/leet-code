# Last updated: 7/28/2026, 1:48:29 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        res=[0]*n
5        pre=1
6        for i in range(n):
7            res[i]=pre
8            pre*=nums[i]
9        suf=1
10        for i in range(n-1,-1,-1):
11            res[i]*=suf
12            suf*=nums[i]
13        return res