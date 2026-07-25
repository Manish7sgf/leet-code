# Last updated: 7/25/2026, 10:55:50 AM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        s=list(str(n))
4        s.sort()
5        return int(s[-1])*int(s[-2])