# Last updated: 10/5/2026, 2:41:24 PM
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sc=d=0
        for i in range(len(s)):
            if s[i]=='(':
                d+=1
            else:
                d-=1
                if s[i-1]=='(':
                    sc+=1<<d
        return sc