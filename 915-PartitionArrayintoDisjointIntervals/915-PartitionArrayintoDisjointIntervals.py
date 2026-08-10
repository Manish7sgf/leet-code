# Last updated: 8/10/2026, 11:37:22 AM
1class Solution:
2    def partitionDisjoint(self, nums: List[int]) -> int:
3        left=nums[0]
4        max_v=nums[0]
5        a=1
6        for i in range(1,len(nums)):
7            max_v=max(max_v,nums[i])
8            if nums[i]<left:
9                left=max_v
10                a=i+1
11        return a