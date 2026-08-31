# Last updated: 8/31/2026, 1:56:58 PM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        og=n
        s=0
        m=1
        while n>0:
            t=n%10
            s+=t
            m*=t
            n//=10
        return og%(s+m)==0