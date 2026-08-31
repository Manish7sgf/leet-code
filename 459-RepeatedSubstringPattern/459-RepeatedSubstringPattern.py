# Last updated: 8/31/2026, 1:58:48 PM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]