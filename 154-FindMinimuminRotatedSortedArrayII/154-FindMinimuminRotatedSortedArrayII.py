# Last updated: 7/20/2026, 3:01:03 PM
1class Solution:
2    def minDistance(self, w1: str, w2: str) -> int:
3        if w1==w2:
4            return 0
5        if len(w1)==len(w2)==1:
6            return 2
7        m=len(w1)
8        n=len(w2)
9        dp=[[0]*(n+1) for _ in range(m+1)]
10        for i in range(m+1):
11            dp[i][0]=i
12        for i in range(n+1):
13            dp[0][i]=i
14        for i in range(1,m+1):
15            for j in range(1,n+1):
16                if w1[i-1]==w2[j-1]:
17                    dp[i][j]=dp[i-1][j-1]
18                else:
19                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
20        return dp[-1][-1]