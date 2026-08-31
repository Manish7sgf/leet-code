# Last updated: 8/31/2026, 1:59:27 PM
class Solution:
    def calculate(self, s: str) -> int:
        a=[]
        n=0
        sign='+'
        for i in range(len(s)):
            if s[i].isdigit():
                n=n*10+int(s[i])
            if (not s[i].isdigit() and s[i]!=' ') or i==len(s)-1:
                if sign=='+':
                    a.append(n)
                elif sign=='-':
                    a.append(-n)
                elif sign=='*':
                    a[-1]*=n
                elif sign=='/':
                    a[-1]=int(a[-1]/n)
                sign=s[i]
                n = 0
        return sum(a)
