# Last updated: 8/31/2026, 1:58:31 PM
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        if w1==w2:
            return 0
        if len(w1)==len(w2)==1:
            return 2
        m=len(w1)
        n=len(w2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for i in range(n+1):
            dp[0][i]=i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if w1[i-1]==w2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]