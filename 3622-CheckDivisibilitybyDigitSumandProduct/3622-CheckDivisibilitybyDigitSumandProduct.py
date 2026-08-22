# Last updated: 8/22/2026, 10:25:15 AM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        og=n
4        s=0
5        m=1
6        while n>0:
7            t=n%10
8            s+=t
9            m*=t
10            n//=10
11        return og%(s+m)==0