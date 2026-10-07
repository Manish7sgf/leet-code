# Last updated: 10/7/2026, 3:56:57 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        add = 0
        for c in s:
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    add += 1
        return add + open