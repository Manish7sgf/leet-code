# Last updated: 7/14/2026, 2:18:33 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        sv={
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        t=0
        for i in range(len(s)):
            c=sv[s[i]]
            if i+1<len(s):
                n=sv[s[i+1]]
                if c<n:
                    t-=c
                else:
                    t+=c
            else:
                t+=c
        return t