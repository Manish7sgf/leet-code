# Last updated: 8/31/2026, 1:57:51 PM
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, ans = 0,0                    
        for digit in s:                     
            if digit =='1':ones+=1       
            elif ones:               
                ones-=1
                ans+=1
        return ans