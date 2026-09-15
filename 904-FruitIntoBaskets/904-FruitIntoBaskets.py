# Last updated: 9/15/2026, 11:07:58 AM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        c={}
        a=0
        for i in range(len(fruits)):
            c[fruits[i]]=c.get(fruits[i],0)+1

            while len(c)>2:
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l+=1
            a=max(a,i-l+1)
        return a