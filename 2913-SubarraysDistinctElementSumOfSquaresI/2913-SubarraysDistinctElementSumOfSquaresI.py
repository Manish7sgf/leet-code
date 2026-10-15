# Last updated: 10/15/2026, 9:54:02 AM
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        tot=0
        n=len(nums)
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                c=len(seen)
                tot+=c*c
        return tot