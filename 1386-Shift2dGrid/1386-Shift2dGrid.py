# Last updated: 8/31/2026, 1:57:35 PM
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m= len(grid)
        n=len(grid[0])
        total=m*n
        k%=total
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                oldIdx=i*n+j
                newIdx=(oldIdx+k)%total
                row=newIdx//n
                col=newIdx%n
                ans[row][col]=grid[i][j]
        return ans