# Last updated: 7/20/2026, 3:08:05 PM
1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m= len(grid)
4        n=len(grid[0])
5        total=m*n
6        k%=total
7        ans=[[0]*n for _ in range(m)]
8        for i in range(m):
9            for j in range(n):
10                oldIdx=i*n+j
11                newIdx=(oldIdx+k)%total
12                row=newIdx//n
13                col=newIdx%n
14                ans[row][col]=grid[i][j]
15        return ans