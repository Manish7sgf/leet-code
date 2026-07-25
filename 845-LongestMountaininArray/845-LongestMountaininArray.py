# Last updated: 7/25/2026, 11:57:28 AM
1class Solution:
2    def longestMountain(self, a: List[int]) -> int:
3        return max((k+l+1 for (q,k),(p,l) in pairwise(
4            (q,abs(sum(g))) for q,g in groupby((v<u)-(v>u) for v,u in pairwise(a))) 
5                if q==1==-p),default=0)