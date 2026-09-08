# Last updated: 9/8/2026, 10:18:54 AM
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