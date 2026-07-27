# Last updated: 7/27/2026, 12:29:39 PM
1from typing import List
2class Solution:
3    def checkPossibility(self, nums:List[int]) -> bool:
4        n=len(nums)
5        chan=0
6        for i in range(n-1):
7            if nums[i]>nums[i+1]:
8                chan+=1
9                if chan>1:
10                    return False
11                
12                if i==0 or nums[i-1]<=nums[i+1]:
13                    nums[i]=nums[i+1]
14                else:
15                    nums[i+1]=nums[i]
16        return True