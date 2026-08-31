# Last updated: 8/31/2026, 1:59:23 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pre=1
        for i in range(n):
            res[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(n-1,-1,-1):
            res[i]*=suf
            suf*=nums[i]
        return res