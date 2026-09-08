# Last updated: 9/8/2026, 10:20:01 AM
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, ans = 0,0                    
        for digit in s:                     
            if digit =='1':ones+=1       
            elif ones:               
                ones-=1
                ans+=1
        return ans