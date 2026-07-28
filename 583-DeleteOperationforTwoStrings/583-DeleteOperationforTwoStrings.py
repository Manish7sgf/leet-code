# Last updated: 7/28/2026, 1:41:55 PM
1class Solution:
2    def arrayNesting(self, nums: List[int]) -> int:
3        res=0
4        l=len(nums)
5        gset=set()
6        for k in range(l):
7            if k not in gset:
8                currlen,currset,val=0,set(),k
9                while True:
10                    if nums[val] in currset: break
11                    currset.add(nums[val])
12                    gset.add(nums[val])
13                    currlen,val=currlen+1,nums[val]
14                res=max(res,currlen)
15        return res