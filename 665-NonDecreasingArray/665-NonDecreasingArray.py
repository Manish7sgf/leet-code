# Last updated: 8/31/2026, 1:58:17 PM
from typing import List
class Solution:
    def checkPossibility(self, nums:List[int]) -> bool:
        n=len(nums)
        chan=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                chan+=1
                if chan>1:
                    return False
                
                if i==0 or nums[i-1]<=nums[i+1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
        return True