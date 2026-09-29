# Last updated: 9/29/2026, 10:09:12 AM
class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate((c == "(") - (c == ")") for c in s))