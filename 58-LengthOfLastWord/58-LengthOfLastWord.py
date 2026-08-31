# Last updated: 8/31/2026, 2:00:52 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        w=s.split()
        l=(w[-1])
        return len(l)