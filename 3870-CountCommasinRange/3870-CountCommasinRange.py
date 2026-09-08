# Last updated: 9/8/2026, 10:14:34 AM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        if n<1000:
4            return 0
5        return n-999