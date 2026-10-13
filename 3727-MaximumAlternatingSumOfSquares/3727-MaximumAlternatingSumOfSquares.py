# Last updated: 10/13/2026, 9:12:06 AM
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a= sorted(b*b for b in nums)
        return sum(a)-sum(a[:len(a)//2])*2