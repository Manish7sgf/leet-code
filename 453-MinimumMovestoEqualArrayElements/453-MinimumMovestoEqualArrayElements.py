# Last updated: 7/30/2026, 11:48:27 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        l=h=0
4        for i in s:
5            l+=1 if i=='(' else -1
6            h+=1 if i!=')' else -1
7            if h < 0:
8                return False
9            l =max(l,0)
10        return l==0