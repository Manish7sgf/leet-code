# Last updated: 8/31/2026, 1:57:26 PM
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n=len(stones)
        for i in range(1,n):
            stones[i]+=stones[i-1]
        a=stones[n-1]
        for i in range(n-2,0,-1):
            a=max(a,stones[i]-a)
        return a