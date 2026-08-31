# Last updated: 8/31/2026, 1:58:45 PM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r={0:-1}
        t=0
        for i in range(len(nums)):
            t+=nums[i]
            rem=t%k
            if rem in r:
                if i-r[rem]>=2:
                    return True
            else:
                r[rem]=i
        return False