# Last updated: 9/8/2026, 10:18:26 AM
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        return n-999