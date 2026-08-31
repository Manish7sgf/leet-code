# Last updated: 8/31/2026, 1:57:52 PM
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left=nums[0]
        max_v=nums[0]
        a=1
        for i in range(1,len(nums)):
            max_v=max(max_v,nums[i])
            if nums[i]<left:
                left=max_v
                a=i+1
        return a