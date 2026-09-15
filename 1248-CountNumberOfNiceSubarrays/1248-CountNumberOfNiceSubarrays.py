# Last updated: 9/15/2026, 11:07:42 AM
class Solution:
    def numberOfSubarrays(self, nums, k):
        left=0
        odd=0
        ans=0
        c=0
        for right in range(len(nums)):
            if nums[right]%2:
                odd+=1
                c=0
            while odd==k:
                if nums[left]%2:
                    odd-=1
                left+=1
                c+= 1
            ans+=c
        return ans