# Last updated: 9/15/2026, 11:07:16 AM
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()
        l=len(digits)
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if i!=j and i!=k and j!=k:
                        if digits[i]!=0 and digits[k]%2==0:
                            n=digits[i]*100+digits[j]*10+digits[k]
                            ans.add(n)
        return len(ans)