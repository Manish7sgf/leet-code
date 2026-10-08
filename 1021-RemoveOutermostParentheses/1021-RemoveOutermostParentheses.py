# Last updated: 10/8/2026, 9:44:44 AM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r=[]
        d=0
        for i in s:
            if i=='(':
                if d>0:
                    r.append(i)
                d+=1
            else:
                d-=1
                if d>0:
                    r.append(i)
        return ''.join(r)