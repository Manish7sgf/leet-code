# Last updated: 10/9/2026, 10:00:08 PM
class Solution:
    def minInsertions(self, s: str) -> int:
        t = s.replace('))','}')
        p = [0,*accumulate(map(' ('.find,t))]
        return t.count(')')+p[-1]*2-min(p)*3