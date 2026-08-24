# Last updated: 8/24/2026, 11:39:16 AM
1class Solution:
2    def stoneGameVIII(self, stones: List[int]) -> int:
3        n=len(stones)
4        for i in range(1,n):
5            stones[i]+=stones[i-1]
6        a=stones[n-1]
7        for i in range(n-2,0,-1):
8            a=max(a,stones[i]-a)
9        return a