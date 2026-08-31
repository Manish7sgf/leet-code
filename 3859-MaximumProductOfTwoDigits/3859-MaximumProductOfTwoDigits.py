# Last updated: 8/31/2026, 1:57:00 PM
class Solution:
    def maxProduct(self, n: int) -> int:
        s=list(str(n))
        s.sort()
        return int(s[-1])*int(s[-2])