# Last updated: 9/30/2026, 9:42:25 AM
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans=[0]*len(seq)
        d=0
        for i, c in enumerate(seq):
            if c=='(':
                d+=1
                ans[i]=d%2
            else:
                ans[i]=d%2
                d-=1
        return ans