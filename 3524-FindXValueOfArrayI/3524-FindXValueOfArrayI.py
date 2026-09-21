# Last updated: 9/21/2026, 11:18:05 AM
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res=[0]*k
        dp=[0]*k
        for num in nums:
            r=num%k
            new_dp=[0]*k
            new_dp[r]+=1
            for x in range(k):
                if dp[x]:
                    new_dp[(x*r)%k]+=dp[x]
            dp = new_dp
            for x in range(k):
                res[x]+=dp[x]
        return res