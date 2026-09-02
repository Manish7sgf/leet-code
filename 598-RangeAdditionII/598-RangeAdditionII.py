# Last updated: 9/2/2026, 5:46:52 PM
1class Solution:
2    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
3        if not ops:
4            return m*n
5        minX=min(op[0] for op in ops)
6        minY=min(op[1] for op in ops)
7        return minX*minY