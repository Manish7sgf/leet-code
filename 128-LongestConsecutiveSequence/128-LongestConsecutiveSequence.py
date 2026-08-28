# Last updated: 8/28/2026, 10:59:43 AM
1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        r={0:-1}
4        t=0
5        for i in range(len(nums)):
6            t+=nums[i]
7            rem=t%k
8            if rem in r:
9                if i-r[rem]>=2:
10                    return True
11            else:
12                r[rem]=i
13        return False